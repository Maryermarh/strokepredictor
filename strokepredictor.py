import streamlit as st
import numpy as np 
import pickle
import sklearn

#load the model 
with open('stroke_model.pkl','rb') as file:
    model = pickle.load(file)
 # streamlit UI
st.title('stroke Prediction App')
st.markdown("""
### **🩺 Discover Your Stroke Risk with My Prediction App!**  
This app helps predict the likelihood of a stroke based on medical and lifestyle inputs.  
Fill in the details below and click **Predict** to see your results.  
""")


#input form
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=120, value=45, step=1)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ["No", "Yes"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"])
Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0, step=0.1)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
smoking_status = st.selectbox("Smoking Status", ["Never smoked", "Formerly smoked", "Smokes", "Unknown"])


# Convert categorical variables to numerical values
sex = 1 if sex == "Male" else 0
ever_married = 1 if ever_married == "Yes" else 0
work_type_mapping = {"Private": 0, "Self-employed": 1, "Govt_job": 2, "Children": 3, "Never_worked": 4}
work_type = work_type_mapping[work_type]
Residence_type = 1 if Residence_type == "Urban" else 0
smoking_mapping = {"Never smoked": 0, "Formerly smoked": 1, "Smokes": 2, "Unknown": 3}
smoking_status = smoking_mapping[smoking_status]

# Prepare input data
input_data = np.array([[sex, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])

#prediction
if st.button("Stroke"):
    prediction = model.predict(input_data)
    st.success(f"Stroke Prediction: {'Yes' if prediction[0] == 1 else 'No'}")


#footer
st.write('NOTE: The risk of having a stroke depends on various factors, including lifestyle, medical history, and age, with older age being a significant determinant. Please consult a healthcare professional for medical advice.')


st.write('Click-On Kaduna DSFP')
st.write('By: Maryam Ibrahim Hamza')
