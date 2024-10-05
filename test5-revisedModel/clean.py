import os
import pandas as pd

# Define the directory where the CSV file is located
directory = '/Users/evandabest/projects/citi/test5-revisedModel'

# Construct the full path to the CSV file
csv_file_path = os.path.join(directory, 'JC-202310-citibike-tripdata.csv')

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Convert 'started_at' to a datetime object for easier time manipulation
df['started_at'] = pd.to_datetime(df['started_at'])

# Define the target station (for which we want to predict availability)
target_station = 'City Hall'

# Step 2: Filter the DataFrame for rows with start or end station as the target station
station_df = df[(df['start_station_name'] == target_station) | (df['end_station_name'] == target_station)].copy()

# Step 3: Extract Time Features (hour of day and day of week)
station_df.loc[:, 'hour'] = station_df['started_at'].dt.hour
station_df.loc[:, 'day_of_week'] = station_df['started_at'].dt.dayofweek

# Step 4: Add Ride History (Lag) Features
# Count the number of rides starting and ending in the past 1, 2, and 3 hours
station_df = station_df.sort_values(by='started_at')

# Create rolling window features for past ride counts (lag features)
station_df.set_index('started_at', inplace=True)
station_df['rides_last_1h'] = station_df['start_station_name'].rolling('1h').count()
station_df['rides_last_2h'] = station_df['start_station_name'].rolling('2h').count()
station_df['rides_last_3h'] = station_df['start_station_name'].rolling('3h').count()
station_df.reset_index(inplace=True)

# Drop NaN values that result from rolling operations
station_df = station_df.dropna()

# Save the filtered DataFrame to a CSV for later use
output_file_path = os.path.join(directory, f'{target_station}_prepared_data.csv')
station_df.to_csv(output_file_path, index=False)

print(f"Data for {target_station} station prepared and saved to '{output_file_path}'.")