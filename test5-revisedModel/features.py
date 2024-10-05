import pandas as pd
import os

# Load the feature-engineered data
directory = '/Users/evandabest/projects/citi/test5-revisedModel'
csv_file_path = os.path.join(directory, 'City Hall_prepared_data.csv')
df = pd.read_csv(csv_file_path)

# Convert 'started_at' to datetime format
df['started_at'] = pd.to_datetime(df['started_at'])

# Step 1: Create a new DataFrame to check electric bike availability at each station
availability_data = df.groupby(['start_station_name', df['started_at'].dt.floor('h')]) \
                       .agg({'rideable_type': 'max'}).reset_index()

# Step 2: Create a target variable indicating availability
availability_data['is_electric_available'] = availability_data['rideable_type'].apply(lambda x: 1 if x == 1 else 0)

# Step 3: Create time-based features
availability_data['hour'] = availability_data['started_at'].dt.hour
availability_data['day_of_week'] = availability_data['started_at'].dt.dayofweek
availability_data['is_weekend'] = availability_data['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# Step 4: Ensure the DataFrame is sorted by 'started_at' for rolling operations
availability_data = availability_data.sort_values(by='started_at')

# Step 5: Create rolling window features for past ride counts (for last 1, 2, and 3 hours)
availability_data.set_index('started_at', inplace=True)
availability_data['rides_last_1h'] = availability_data['is_electric_available'].rolling('1h').sum()
availability_data['rides_last_2h'] = availability_data['is_electric_available'].rolling('2h').sum()
availability_data['rides_last_3h'] = availability_data['is_electric_available'].rolling('3h').sum()
availability_data.reset_index(inplace=True)

# Clean up NaN values resulting from rolling operations
availability_data = availability_data.dropna()

# Step 6: Save the aggregated data to a new CSV
output_file_path = os.path.join(directory, 'City_Hall_availability_data.csv')
availability_data.to_csv(output_file_path, index=False)

print(f"Availability data saved to '{output_file_path}'")