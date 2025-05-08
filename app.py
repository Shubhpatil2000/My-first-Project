import streamlit as st
import joblib
import numpy as np

# Load the saved regression model
model = joblib.load('regression_model.joblib')

# Streamlit app UI
st.title("Salary Prediction Based on Years of Experience")
st.write("Enter your years of experience to predict the expected salary.")

# User input for Years of Experience
years_exp = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

# Predict button
if st.button("Predict Salary"):
    # Prepare input data for the model
    input_data = np.array([[years_exp]])

    # Predict the salary
    prediction = model.predict(input_data)
    predicted_salary = float(prediction[0])  # Convert NumPY value to float

    # Show the result
    st.success(f"Predicted Salary: ₹{predicted_salary:,.2f} per annum")
