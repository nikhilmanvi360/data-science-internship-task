# Task 3: Student Course Purchase Prediction

This project uses Machine Learning to predict whether a student will purchase a new online course based on their platform activity and learning behavior.

## Dataset Features
- **Age**: Student's age.
- **Study Hours per Week**: Hours spent studying on the platform.
- **Previous Courses Completed**: Total courses successfully finished.
- **Platform Visits per Month**: Frequency of platform engagement.
- **Assignment Completion Rate**: Percentage of assignments completed.
- **Purchased Course**: The target variable (1 = Likely, 0 = Unlikely).

## Implementation Details
- **Model**: `RandomForestClassifier`
- **Pre-processing**: Feature scaling using `StandardScaler`.
- **Accuracy**: 78%
- **Interface**: Built with Streamlit for a premium user experience.

## Project Structure
- `train_model.py`: Script to preprocess data, train the model, and save joblib assets.
- `app.py`: Streamlit application for real-time predictions.
- `model.joblib`: Trained classification model.
- `scaler.joblib`: Trained feature scaler.
- `edtech_student_course_purchase_dataset.csv`: Source dataset.

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas scikit-learn joblib streamlit
   ```
2. Run the training script:
   ```bash
   python train_model.py
   ```
3. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
