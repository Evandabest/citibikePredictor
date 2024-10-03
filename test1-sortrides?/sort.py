import pandas as pd

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/Users/evandabest/projects/citi/test1-sortrides?/JC-202310-citibike-tripdata-reduced-updated.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Sort the DataFrame by the 'start_station_name' column
df_sorted = df.sort_values(by='start_station_name')

# Step 3: Save the sorted DataFrame back to a CSV file
output_file_path = '/Users/evandabest/projects/citi/test1-sortrides?/JC-202310-citibike-tripdata-sorted.csv'
df_sorted.to_csv(output_file_path, index=False)

print("Sorted file 'JC-202310-citibike-tripdata-sorted.csv' created successfully.")