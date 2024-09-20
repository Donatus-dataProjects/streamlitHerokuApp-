# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:50:43 2024

@author: DONATUS
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu 

#loading the saved models and since they are in the same directory I don't need to specify their path again.
#for diabetes model
diabetes_model = pickle.load(open("diabetes_trained_model.sav", 'rb'))

#for heart model
heart_model = pickle.load(open("heart_trained_model.sav", 'rb'))

#side-bar navigation
with st.sidebar:
    
    #creating a function for my option menu
    selected = option_menu('Multiple Disease Prediction System Using ML',
                           ['Diabetes Predcition', 'Heart Prediction'],
                           icons = ['activity', 'lungs-fill'],
                           default_index = 0)
    
    #Diabetes Prediction Page
if (selected == 'Diabetes Predcition'):
    #Page title
    st.title('Diabetes Prediction Using ML')
    #Getting the input from the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Body Mass Index')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age of the Person')
    
    
    
    #code for prediction, creating and empty string that will save my end result of the prediction
    diab_diagnosis = '' #After prediction the string output will be return in the string.
    
    
    #Creating a pattern for prediction with an if condition 
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                         Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        #My Predictive System
        if (diabetes_prediction[0] == 1):
            diab_diagnosis = 'The Person is Diabetic'
        
        else:
            diab_diagnosis = 'The person is Not Diabetic'
        
        st.success(diab_diagnosis)
    

# Heart Prediction Page
if selected == 'Heart Prediction':
    # Page title
    st.title('Heart Prediction Using ML')
    
    # Getting the input from the user
    age = st.text_input('Age of Person')
    sex = st.text_input('Gender of Person (0 for female, 1 for male)')
    resting_bp = st.text_input('Resting Blood Pressure')
    chest_pain_type = st.text_input('Chest Pain Type')
    cholestoral = st.text_input('Cholesterol')
    fasting_blood_sugar = st.text_input('Fasting Blood Sugar')
    restecg = st.text_input('Resting Electrocardiogram')
    max_hr = st.text_input('Maximum Heart Rate')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('Oldpeak')
    slope = st.text_input('Slope')
    num_major_vessels = st.text_input('Number of Major Blood Vessels')
    thal = st.text_input('Thalassemia Status')
    
    # Code for prediction
    if st.button('Heart Test Result'):
        # Converting input data to the correct datatypes since Logistics model could'nt conver my data types to float and int as other models like SVC
        input_data = [
            int(age),
            int(sex),
            float(resting_bp),
            int(chest_pain_type),
            float(cholestoral),
            int(fasting_blood_sugar),
            int(restecg),
            float(max_hr),
            int(exang),
            float(oldpeak),
            int(slope),
            int(num_major_vessels),
            int(thal)
        ]
        
        # Making a prediction
        heart_prediction = heart_model.predict([input_data])
        
        # My Predictive System
        if heart_prediction[0] == 1:
            hrt_diagnosis = 'The Person is at Risk of Heart Disease'
        else:
            hrt_diagnosis = 'The Person is Not at Risk of Heart Disease'
        
        st.success(hrt_diagnosis)