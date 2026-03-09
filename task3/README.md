# 🎓 EdTech Student Course Purchase Predictor

A premium machine learning application designed to predict the likelihood of students enrolling in new online courses based on their platform activity and learning patterns.

## 🚀 Overview

This project leverages data-driven insights to help EdTech platforms optimize their marketing strategies and improve student engagement. By analyzing historical behavior, our model proactively identifies students who are most likely to purchase a new course.

## ✨ Key Features

- **Premium Interface**: Built with Streamlit for a sleek, responsive, and user-friendly experience.
- **Real-time Prediction**: Instantly assess purchase likelihood with a confidence score.
- **Intelligent Modeling**: Powered by a Robust `RandomForestClassifier` trained on behavioral datasets.
- **Data Insights**: Analyzes key metrics such as study hours, assignment completion rates, and platform visits.

## 🛠️ Tech Stack

- **Language**: Python 3
- **Analysis**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn (Random Forest)
- **Model Storage**: Joblib
- **Frontend**: Streamlit

## 📁 Project Structure

```text
├── app.py                   # Streamlit application for real-time predictions
├── train_model.py         # Model training and data preprocessing script
├── model.joblib             # Saved Random Forest model
├── scaler.joblib            # Trained feature scaler
├── edtech_student_...csv     # Student behavior dataset
└── README.md                # Project documentation
```

## ⚙️ Installation & Usage

### 1. Requirements
Ensure you have Python installed, then install the necessary dependencies:
```bash
pip install pandas scikit-learn joblib streamlit
```

### 2. Model Training
To retrain the model or update the assets:
```bash
python train_model.py
```

### 3. Launching the App
Start the Streamlit dashboard:
```bash
streamlit run app.py
```

## 📊 Model Performance

- **Primary Algorithm**: Random Forest Classifier
- **Preprocessing**: Feature scaling using `StandardScaler`
- **Evaluation**: The model achieves high precision and recall, ensuring reliable marketing insights.

---
*Developed for the Data Science Internship Task*
