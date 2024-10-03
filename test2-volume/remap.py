import pandas as pd

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/Users/evandabest/projects/citi/test2-volume/JC-202310-citibike-tripdata-reduced.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Replace 'classic_bike' with 0 and 'electric_bike' with 1
df['rideable_type'] = df['rideable_type'].replace({'classic_bike': 0, 'electric_bike': 1})

# Step 3: Save the modified DataFrame back to a CSV file
output_file_path = '/Users/evandabest/projects/citi/test2-volume/JC-202310-citibike-tripdata-reduced-updated.csv'
df.to_csv(output_file_path, index=False)

print("Updated file 'JC-202310-citibike-tripdata-reduced-updated.csv' created successfully.")