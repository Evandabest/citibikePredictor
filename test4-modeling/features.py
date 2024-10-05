import pandas as pd
import os

# Step 1: Load the prepared data from CSV
directory = '/Users/evandabest/projects/citi/test4-modeling'
csv_file_path = os.path.join(directory, 'City Hall_prepared_data.csv')

df = pd.read_csv(csv_file_path)

# Convert 'started_at' to datetime format
df['started_at'] = pd.to_datetime(df['started_at'])

# Step 2: Time-based Features
df['hour'] = df['started_at'].dt.hour
df['day_of_week'] = df['started_at'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# Step 3: Rideable Type Feature (0 for classic bike, 1 for electric bike)
df['rideable_type'] = df['rideable_type'].replace({'classic_bike': 0, 'electric_bike': 1}).infer_objects(copy=False)

# Step 4: Member vs Casual Feature (1 for member, 0 for casual)
df['member_type'] = df['member_casual'].replace({'member': 1, 'casual': 0}).infer_objects(copy=False)

# Step 5: Lag Features (Ride History)
# Create rolling window features for past ride counts (for last 1, 2, and 3 hours)
df = df.sort_values(by='started_at')
df.set_index('started_at', inplace=True)
df['rides_last_1h'] = df['start_station_name'].rolling('1h').count()
df['rides_last_2h'] = df['start_station_name'].rolling('2h').count()
df['rides_last_3h'] = df['start_station_name'].rolling('3h').count()
df.reset_index(inplace=True)

# Clean up NaN values resulting from rolling operations
df = df.dropna()

# Step 6: Save the feature-engineered dataset to a new CSV
output_file_path = os.path.join(directory, 'City_Hall_feature_engineered.csv')
df.to_csv(output_file_path, index=False)

print(f"Feature-engineered data saved to '{output_file_path}'")