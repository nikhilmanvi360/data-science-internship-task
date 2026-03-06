import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="EdTech Course Purchase Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    .prediction-card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 20px;
    }
    .likely {
        color: #28a745;
        font-weight: bold;
        font-size: 1.5em;
    }
    .unlikely {
        color: #dc3545;
        font-weight: bold;
        font-size: 1.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model and scaler
@st.cache_resource
def load_assets():
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib')
    return model, scaler

try:
    model, scaler = load_assets()
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")
    st.stop()

# Header
st.title("🎓 Course Purchase Predictor")
st.markdown("Predict whether a student is likely to enroll in a new course based on their platform activity.")

# Input Form
with st.container():
    st.subheader("Student Details")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=12, max_value=100, value=22)
        study_hours = st.number_input("Study Hours per Week", min_value=0, max_value=168, value=14)
        previous_courses = st.number_input("Previous Courses Completed", min_value=0, max_value=50, value=3)
        
    with col2:
        platform_visits = st.number_input("Platform Visits per Month", min_value=0, max_value=200, value=20)
        assignment_completion = st.slider("Assignment Completion Rate (%)", min_value=0, max_value=100, value=85)

# Prediction Logic
if st.button("Predict Purchase Likelihood"):
    # Prepare input data
    input_data = pd.DataFrame([[
        age, 
        study_hours, 
        previous_courses, 
        platform_visits, 
        assignment_completion
    ]], columns=['age', 'study_hours_per_week', 'previous_courses_completed', 'platform_visits_per_month', 'assignment_completion_rate'])
    
    # Scale input data
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    prediction_proba = model.predict_proba(input_scaled)[0][1]
    
    # Display Results
    st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
    if prediction == 1:
        st.markdown('<h3>Result:</h3>', unsafe_allow_html=True)
        st.markdown('<p class="likely">Student Likely to Purchase Course</p>', unsafe_allow_html=True)
        st.write(f"Confidence score: {prediction_proba:.2%}")
    else:
        st.markdown('<h3>Result:</h3>', unsafe_allow_html=True)
        st.markdown('<p class="unlikely">Student Unlikely to Purchase Course</p>', unsafe_allow_html=True)
        st.write(f"Confidence score: {(1 - prediction_proba):.2%}")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6c757d;'>EdTech Platform - Marketing Analytics Tool</p>", unsafe_allow_html=True)
