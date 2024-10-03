import pandas as pd

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/Users/evandabest/projects/citi/test2-volume/JC-202310-citibike-tripdata-filtered.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Filter the DataFrame for electric bikes (rideable_type == 1) and start station 'Brunswick St'
electric_bikes_df = df[(df['rideable_type'] == 1) & (df['start_station_name'] == 'Brunswick St')]

# Step 3: Convert 'started_at' to datetime and extract the hour
electric_bikes_df['started_at'] = pd.to_datetime(electric_bikes_df['started_at'])
electric_bikes_df['hour'] = electric_bikes_df['started_at'].dt.hour

# Step 4: Aggregate the data to get the average number of electric bikes for each hour
hourly_average = electric_bikes_df.groupby('hour').size().reset_index(name='count')
hourly_average['average'] = hourly_average['count'] / len(electric_bikes_df['hour'].unique())

# Step 5: Print the results
print(hourly_average[['hour', 'average']])

