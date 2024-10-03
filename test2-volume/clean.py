import os
import pandas as pd

# Define the directory where the CSV file is located
directory = '/Users/evandabest/projects/citi/test2-volume'

# Construct the full path to the CSV file
csv_file_path = os.path.join(directory, 'JC-202310-citibike-tripdata.csv')

# Step 2: Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Step 3: Drop the specified columns
columns_to_drop = [
    'ride_id', 'ended_at', 'start_station_id', 
    'end_station_id', 'start_lat', 
    'start_lng', 'end_lat', 'end_lng'
]
df_reduced = df.drop(columns=columns_to_drop)

# Step 4: Save the reduced DataFrame to a new CSV file
output_file_path = os.path.join(directory, 'JC-202310-citibike-tripdata-reduced.csv')
df_reduced.to_csv(output_file_path, index=False)

print("New file 'JC-202310-citibike-tripdata-reduced.csv' created successfully.")
