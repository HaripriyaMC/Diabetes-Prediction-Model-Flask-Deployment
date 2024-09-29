import requests

# Replace the URL with your actual Flask server URL
url = 'http://localhost:5000/predict_api'

# Example input data for diabetes prediction
data = {
    'gender': 'Male',
    'age': 45,
    'hypertension': 0,
    'heart_disease': 1,
    'smoking_history': 'never',
    'bmi': 28.5,
    'HbA1c_level': 5.8,
    'blood_glucose_level': 130
}

# Make a POST request to the Flask server
r = requests.post(url, json=data)

# Print the prediction result from the server
print(r.json())
