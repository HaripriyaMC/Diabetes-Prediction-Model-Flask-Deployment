## Diabetes-Prediction-Model-Flask-Deployment
This is a demo project to demonstrate how a Machine Learning model for predicting diabetes can be deployed using a Flask API.

### Prerequisites
To run this project, you must have the following Python libraries installed:
- Scikit Learn
- Pandas
- Flask
- NumPy


This project has four major parts:

1. **model.py**  
   This script contains the code to train the Machine Learning model for diabetes prediction based on the dataset provided. It also saves the trained model as a serialized `.pkl` file.

2. **app.py**  
   This script contains the Flask APIs that receive patient data via the HTML GUI or API calls, run the data through the trained machine learning model, and return whether the patient is likely to have diabetes.

3. **request.py**  
   This script uses the `requests` module to send POST requests to the Flask API and displays the result returned by the model.

4. **templates**  
   This folder contains the HTML template (index.html), allowing the user to input patient details (such as age, BMI, HbA1c level, etc.) and view the predicted diabetes status.

### Running the Project
1. **Train the model**  
   Ensure you are in the project directory and run the following command to train the model and save it to a file named `diabetes_model.pkl`:
   ```bash
   python model.py
   ```

2. **Run the Flask App**  
   Start the Flask API by running the following command:
   ```bash
   python app.py
   ```


3. **Access the Web Interface**  
Navigate to URL http://localhost:5000

You should see the homepage where you can input patient details like age, BMI, blood glucose level, etc.

4. **Predict Diabetes** 
Enter valid numerical values for all input fields and click "Predict". The result will show whether the patient is likely to have diabetes or not.



4. **Send API Requests**  
You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```

### Example
When the model predicts a high risk of diabetes, the web page will display:

```
The patient is likely to have diabetes.
```

If the model predicts a low risk, the result will show:
```
The patient is unlikely to have diabetes.
```
## Dataset Description

The dataset used in this project contains medical information such as age, gender, BMI, hypertension, heart disease, HbA1c level, and blood glucose level. The target variable indicates whether the patient has diabetes or not.

- gender: Male (0), Female (1)
- age: Patient's age
- hypertension: Presence of hypertension (0 = No, 1 = Yes)
- heart_disease: Presence of heart disease (0 = No, 1 = Yes)
- smoking_history: Smoking status (0 = Never, 1 = Former, 2 = Current, 3 = Unknown)
- bmi: Body Mass Index
- HbA1c_level: Glycated hemoglobin level
- blood_glucose_level: Blood glucose level




