import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/Users/evandabest/projects/citi/test2-volume/JC-202310-citibike-tripdata-filtered.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Preprocess the data
# Convert 'started_at' to datetime and extract the hour
df['started_at'] = pd.to_datetime(df['started_at'])
df['hour'] = df['started_at'].dt.hour

# Step 3: Aggregate the data to get the volume of bike usage for each hour
hourly_volume = df.groupby('hour').size().reset_index(name='volume')

# Step 4: Prepare the data for the regression model
X = hourly_volume[['hour']]
y = hourly_volume['volume']

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Step 8: Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Volume')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Predicted Volume')
plt.title('Bike Usage Volume by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Volume')
plt.legend()
plt.show()