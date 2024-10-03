
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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

# Step 3: Split the data into features (X) and target (y)
X = df.drop(columns=['rideable_type'])
y = df['rideable_type']

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)