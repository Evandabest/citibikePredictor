import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data
csv_file_path = '/Users/evandabest/projects/citi/test1-sortrides?/JC-202310-citibike-tripdata-filtered.csv'
df = pd.read_csv(csv_file_path, header=None, names=['rideable_type', 'timestamp', 'start_station_name', 'member_casual'])

# Step 2: Preprocess the data
# Convert 'rideable_type' to numeric (already done in previous steps)
# Convert 'timestamp' to datetime and extract features like hour, day, month
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day
df['month'] = df['timestamp'].dt.month

# Drop unnecessary columns
df = df.drop(columns=['timestamp', 'start_station_name', 'member_casual'])

# Step 3: Visualize the data

# Scatter Plot: Hour vs Rideable Type
plt.figure(figsize=(10, 6))
sns.scatterplot(x='hour', y='rideable_type', data=df)
plt.title('Scatter Plot: Hour vs Rideable Type')
plt.xlabel('Hour')
plt.ylabel('Rideable Type')
plt.show()

# Histogram: Distribution of Rideable Type
plt.figure(figsize=(10, 6))
sns.histplot(df['rideable_type'], bins=30, kde=True)
plt.title('Histogram: Distribution of Rideable Type')
plt.xlabel('Rideable Type')
plt.ylabel('Frequency')
plt.show()

# Pair Plot: Pairwise relationships in the dataset
sns.pairplot(df)
plt.show()