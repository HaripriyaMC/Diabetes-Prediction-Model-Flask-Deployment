# Importing the libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the new dataset (replace 'new_dataset.csv' with the actual path to your new CSV file)
dataset = pd.read_csv(r'D:\My-Projects\Diabetes_Prediction\templates\diabetes_prediction_dataset.csv')

# Handle missing or 'No Info' values in smoking_history by replacing them with a default value, like 'unknown'
dataset['smoking_history'].replace('No Info', 'unknown', inplace=True)

# Filling missing values for BMI, HbA1c_level, and blood_glucose_level if any
dataset['bmi'].fillna(dataset['bmi'].mean(), inplace=True)
dataset['HbA1c_level'].fillna(dataset['HbA1c_level'].mean(), inplace=True)
dataset['blood_glucose_level'].fillna(dataset['blood_glucose_level'].mean(), inplace=True)

# Converting categorical data (gender, smoking_history) into numerical format
dataset['gender'] = dataset['gender'].map({'Male': 0, 'Female': 1})
dataset['smoking_history'] = dataset['smoking_history'].map({'never': 0, 'former': 1, 'current': 2, 'unknown': 3})

# Check if there are any remaining missing values
print("Number of missing values in each column:")
print(dataset.isnull().sum())

# Splitting the features (X) and target variable (y)
X = dataset[['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']]
y = dataset['diabetes']  # Target variable

# Check for any missing values in X before fitting the model
if X.isnull().any().any():
    print("There are missing values in X. Filling them with column means.")
    X = X.fillna(X.mean())  # Fill any remaining NaN values with the mean of the respective columns

# Splitting Training and Test Set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the model using Logistic Regression
model = LogisticRegression()

# Fitting the model
model.fit(X_train, y_train)

# Saving the trained model to disk
pickle.dump(model, open('diabetes_model.pkl', 'wb'))

# Loading the model and making a prediction (for testing purposes)
loaded_model = pickle.load(open('diabetes_model.pkl', 'rb'))
sample_data = [[1, 80, 0, 1, 0, 25.19, 6.6, 140]]  # Sample input data
print(loaded_model.predict(sample_data))
