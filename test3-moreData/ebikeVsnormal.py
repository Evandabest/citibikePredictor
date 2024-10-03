import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the directory where the CSV file is located
directory = '/Users/evandabest/projects/citi/test3-moreData'

# Construct the full path to the CSV file
csv_file_path = os.path.join(directory, 'JC-202310-citibike-tripdata-reduced.csv')

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Step 2: Convert 'started_at' to datetime and extract the hour
df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce')
df = df.dropna(subset=['started_at'])  # Drop rows with invalid 'started_at' values
df['hour'] = df['started_at'].dt.hour

# Step 3: Separate the data into electric bikes and regular bikes
electric_bikes_df = df[df['rideable_type'] == 1]
regular_bikes_df = df[df['rideable_type'] == 0]

# Step 4: Aggregate the data to get the volume of electric bikes and regular bikes for each hour
electric_bikes_hourly = electric_bikes_df.groupby('hour').size().reset_index(name='electric_bike_volume')
regular_bikes_hourly = regular_bikes_df.groupby('hour').size().reset_index(name='regular_bike_volume')

# Step 5: Merge the two DataFrames on 'hour'
hourly_volume = pd.merge(electric_bikes_hourly, regular_bikes_hourly, on='hour', how='outer').fillna(0)

# Step 6: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hourly_volume['hour'], hourly_volume['electric_bike_volume'], marker='o', linestyle='-', label='Electric Bikes')
plt.plot(hourly_volume['hour'], hourly_volume['regular_bike_volume'], marker='x', linestyle='--', label='Regular Bikes')
plt.title('Electric and Regular Bike Usage Volume by Hour of Day at City Hall')
plt.xlabel('Hour of Day')
plt.ylabel('Volume')
plt.xticks(range(0, 24))  # Ensure all hours are shown on the x-axis
plt.legend()
plt.grid(True)
plt.show()

# Step 7: Print the results
print("Hourly Volume DataFrame:")
print(hourly_volume)