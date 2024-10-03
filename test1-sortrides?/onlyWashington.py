import pandas as pd

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/Users/evandabest/projects/citi/test1-sortrides?/JC-202310-citibike-tripdata-sorted.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Filter the DataFrame for rows where 'start_station_name' is '11 St & Washington St' and 'member_casual' is 'casual'
filtered_df = df.loc[(df['start_station_name'] == '11 St & Washington St') & (df['member_casual'] == 'casual')]

# Step 3: Save the filtered DataFrame back to a CSV file
output_file_path = '/Users/evandabest/projects/citi/test1-sortrides?/JC-202310-citibike-tripdata-filtered.csv'
filtered_df.to_csv(output_file_path, index=False)

print("Filtered file 'JC-202310-citibike-tripdata-filtered.csv' created successfully.")