import os
import pandas as pd

# Define the directory where the CSV file is located
directory = '/Users/evandabest/projects/citi/test3-moreData'

# Construct the full path to the CSV file
csv_file_path = os.path.join(directory, 'JC-202310-citibike-tripdata.csv')

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Step 2: Filter the DataFrame for rows with start or end station as 'Brunswick St'
filtered_df = df.loc[
    (df['start_station_name'] == 'City Hall') |
    (df['end_station_name'] == 'City Hall')
]

# Step 3: Drop the specified columns from the filtered DataFrame
columns_to_drop = [
    'ride_id', 'ended_at', 'start_station_id', 
    'end_station_id', 'start_lat', 
    'start_lng', 'end_lat', 'end_lng', 'member_casual'
]
filtered_df_reduced = filtered_df.drop(columns=columns_to_drop)

# Step 4: Replace 'rideable_type' values
filtered_df_reduced['rideable_type'] = filtered_df_reduced['rideable_type'].replace({'classic_bike': 0, 'electric_bike': 1})

# Step 5: Save the reduced DataFrame to a new CSV file
output_file_path = os.path.join(directory, 'JC-202310-citibike-tripdata-reduced.csv')
filtered_df_reduced.to_csv(output_file_path, index=False)

print("New file 'JC-202310-citibike-tripdata-reduced.csv' created successfully.")
