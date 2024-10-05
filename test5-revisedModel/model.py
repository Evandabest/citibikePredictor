from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os
import pandas as pd

directory = '/Users/evandabest/projects/citi/test5-revisedModel'
# Load the availability data
availability_file_path = os.path.join(directory, 'City_Hall_availability_data.csv')
availability_df = pd.read_csv(availability_file_path)

# Define the target variable and features
X = availability_df[['hour', 'day_of_week', 'is_weekend', 'rides_last_1h', 'rides_last_2h', 'rides_last_3h']]
y = availability_df['is_electric_available']  # 1 if electric bike is available, else 0

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Optional: Save the trained model
#import joblib
#model_save_path = os.path.join(directory, 'rf_availability_model.pkl')
#joblib.dump(rf_model, model_save_path)
#print(f"Model saved to '{model_save_path}'")
