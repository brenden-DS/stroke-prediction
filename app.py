import streamlit as st
import numpy as np
import pickle
import pandas as pd


model = pickle.load(open('stroke_rf.sav','rb'))

st.image('stroke_pic.jpg')
st.write("""### The app is developed using a stroke dataset of 5k individuals regarding their health status, utilizing a random forest machine learning algorithm with an accuracy of 95%. Please note that these results do not equate to a medical diagnosis.  
         """)
st.write("""
          ## To predict your likelihood of a stroke status:
          1- Enter the parameters that best describe you.
          
          2- Press the "Predict" button and wait for the result.
         """)

def stroke_prediction(features):
    # Changing the data into a NumPy array and reshaping
    features_as_nparray = np.asarray(features).reshape(1, -1)

    # Making a single prediction
    prediction = model.predict(features_as_nparray)

    message = ""
    if prediction == 0:
        message = "Congratulations! You have a low stroke risk. Based on the provided information, it seems there is no immediate risk of stroke. However, it's always advisable to consult with a healthcare professional for a more accurate assessment."
        st.success(message)
    else:
        message = "Warning! You have a high stroke risk. Based on the provided information, there is a potential risk of stroke. It is strongly recommended to consult with a healthcare professional for a thorough evaluation and guidance on preventive measures."
        st.warning(message)

    return message

# Create a Streamlit web app
def main():
    # Set app title and description

    st.sidebar.write("Enter the required information to predict the likelihood of stroke.")

    # Create input fields for user to enter information
    age = st.sidebar.number_input("Enter your age", min_value=1, max_value=100, value=30)
    hypertension = st.sidebar.selectbox("Do you have hypertension?", ("Yes", "No"))
    heart_disease = st.sidebar.selectbox("Do you have a heart disease?", ("Yes", "No"))
    avg_glucose_level = st.sidebar.number_input("Enter your average glucose level", min_value=0.0, value=80.0)
    bmi = st.sidebar.number_input("Enter your body mass index (BMI)", min_value=0.0, value=20.0)
    gender = st.sidebar.selectbox("Select your gender", ("Male", "Female","Other"))
    smoking_status = st.sidebar.selectbox("Select your smoking status", ("Unknown", "Formerly Smoked", "Never Smoked", "Smokes"))
    ever_married = st.sidebar.selectbox("Have you ever been married?", ("Yes", "No"))
    work_type = st.sidebar.selectbox("Select your work type status", ("Private", "Self-employed", "children", "Govt_job","Never_worked"))
    residence_type = st.sidebar.selectbox("Select your residence type", ("Urban", "Rural"))

    # Convert categorical inputs to numerical values

    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0
    gender = 1 if gender == "Male" else 0
    ever_married = 1 if ever_married == "Yes" else 0
    residence_type = 1 if residence_type == "Urban" else 0

    smoking_map = {"Unknown": 0, "Formerly Smoked": 1, "Never Smoked": 2, "Smokes": 3}
    smoking_status = smoking_map[smoking_status]

    work_type_map = {"Govt_job": 0, "Never_worked": 1, "Private": 2, "Self-employed": 3, "children": 4}
    work_type = work_type_map[work_type]

    diagnosis = ''

    # Making a button for prediction
    if st.button('PREDICT'):
        diagnosis = stroke_prediction([age, hypertension, heart_disease, avg_glucose_level, bmi, gender, smoking_status, ever_married, work_type, residence_type])




# Run the web app
if __name__ == "__main__":
    main()