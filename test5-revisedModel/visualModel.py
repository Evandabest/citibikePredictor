import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the feature-engineered data
file_path = '/Users/evandabest/projects/citi/test5-revisedModel/City_Hall_availability_data.csv'  # Update with actual path
df = pd.read_csv(file_path)

# Inspect the columns in the DataFrame
print("Columns in the DataFrame:", df.columns)

# Define the target variable (whether it's an electric bike) and features
# Update the feature selection based on the actual columns in the DataFrame
X = df[['hour', 'day_of_week', 'is_weekend', 'rides_last_1h', 'rides_last_2h', 'rides_last_3h']]
y = df['rideable_type']  # Target variable: 0 for classic bike, 1 for electric bike

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)

# Train the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=43)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Get the predicted probabilities for the test set
y_prob = rf_model.predict_proba(X_test)[:, 1]  # Probability of class 1 (electric bike)

# Add the predicted probabilities and the actual hour to a DataFrame
results_df = pd.DataFrame({'hour': X_test['hour'], 'probability': y_prob})

# Aggregate the probabilities by hour
hourly_prob = results_df.groupby('hour')['probability'].mean().reset_index()

# Plot the results
plt.figure(figsize=(10, 6))
sns.lineplot(data=hourly_prob, x='hour', y='probability', marker='o')
plt.xlabel('Hour of Day')
plt.ylabel('Probability of Electric Bike Availability')
plt.title('Probability of Electric Bike Availability vs Time of Day for City Hall Station')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()

import joblib

# Save the model to a file
#model_file_path = '/Users/evandabest/projects/citi/test5-revisedModel/rf_model.joblib'  # Update with desired path
#joblib.dump(rf_model, model_file_path)
#print(f"Model saved to '{model_file_path}'")