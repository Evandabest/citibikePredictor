import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Load the feature-engineered data
file_path = '/Users/evandabest/projects/citi/test4-modeling/City_Hall_feature_engineered.csv'  # Update with actual path
df = pd.read_csv(file_path)

# Step 2: Define the target variable (whether it's an electric bike) and features
X = df[['hour', 'day_of_week', 'is_weekend', 'member_type', 'rides_last_1h', 'rides_last_2h', 'rides_last_3h']]
y = df['rideable_type']  # Target variable: 0 for classic bike, 1 for electric bike

# Step 3: Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Step 7: Plot the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Classic Bike', 'Electric Bike'], yticklabels=['Classic Bike', 'Electric Bike'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Optional: Save the trained model for later use
#import joblib
#model_save_path = '/Users/evandabest/projects/citi/test4-modeling/rf_model.pkl'
#joblib.dump(rf_model, model_save_path)
#print(f"Model saved to '{model_save_path}'")