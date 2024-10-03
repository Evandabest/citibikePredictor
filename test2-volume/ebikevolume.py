import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/Users/evandabest/projects/citi/test2-volume/JC-202310-citibike-tripdata-filtered.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Filter the DataFrame for electric bikes (rideable_type == 1)
electric_bikes_df = df[df['rideable_type'] == 1].copy()

# Step 3: Convert 'started_at' to datetime and extract the hour and date
electric_bikes_df['started_at'] = pd.to_datetime(electric_bikes_df['started_at'], errors='coerce')

# Drop rows with invalid 'started_at' values
electric_bikes_df = electric_bikes_df.dropna(subset=['started_at'])

# Extract hour and date
electric_bikes_df['hour'] = electric_bikes_df['started_at'].dt.hour
electric_bikes_df['date'] = electric_bikes_df['started_at'].dt.date

# Step 4: Aggregate the data to get the volume of electric bikes for each hour
hourly_volume = electric_bikes_df.groupby(['date', 'hour']).size().reset_index(name='volume')

# Step 5: Calculate the average volume of electric bikes for each hour
hourly_average = hourly_volume.groupby('hour')['volume'].mean().reset_index(name='average')

# Step 6: Plot the average volume
plt.figure(figsize=(10, 6))
plt.plot(hourly_average['hour'], hourly_average['average'], marker='x', linestyle='--', label='Average Volume')
plt.title('Average Electric Bike Usage Volume by Hour of Day at Brunswick St')
plt.xlabel('Hour of Day')
plt.ylabel('Average Volume')
plt.xticks(range(0, 24))  # Ensure all hours are shown on the x-axis
plt.legend()
plt.grid(True)
plt.show()

# Step 7: Print the results
print(hourly_average[['hour', 'average']])