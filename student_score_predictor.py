import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 1. CREATE DATASET
print("--- 1. Creating Dataset ---")
data = {
    'study_hours': [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10],
    'marks': [35, 45, 50, 55, 58, 65, 68, 72, 75, 78, 82, 85, 88, 92, 95]
}
df = pd.DataFrame(data)

# 2. EXPLORATORY DATA ANALYSIS (EDA)
print("\n--- 2. Exploratory Data Analysis ---")
print("First 5 rows:")
print(df.head())
print("\nShape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nBasic Statistics:")
print(df.describe())

# Plotting (Note: In some environments, plt.show() might not display, but we'll include it)
plt.figure(figsize=(10, 6))
plt.scatter(df['study_hours'], df['marks'], color='blue', label='Actual Data')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study Hours vs Marks')
plt.legend()
plt.grid(True)
plt.savefig('eda_plot.png')
print("\nEDA plot saved as 'eda_plot.png'")

# 3. PREPARE DATA
print("\n--- 3. Preparing Data ---")
X = df['study_hours'].values.reshape(-1, 1) # Reshape to 2D
y = df['marks'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into 80% training and 20% testing sets.")

# 4. TRAIN MODEL
print("\n--- 4. Training Model ---")
model = LinearRegression()
model.fit(X_train, y_train)
print("Linear Regression model trained successfully.")

# 5. EVALUATE MODEL
print("\n--- 5. Evaluating Model ---")
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# 6. VISUALIZE RESULTS
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Linear Regression: Study Hours vs Predicted Marks')
plt.legend()
plt.grid(True)
plt.savefig('regression_results.png')
print("\nRegression visualization saved as 'regression_results.png'")

# 7. PREDICT FUNCTION
print("\n--- 7. Predict Function (Manual Input) ---")
def predict_score(study_hours):
    """Predicts score based on study hours."""
    # Reshape input to 2D for sklearn
    hours_reshaped = np.array([[study_hours]])
    prediction = model.predict(hours_reshaped)[0]
    # Cap the score between 0 and 100
    prediction = max(0, min(100, prediction))
    return round(prediction, 2)

try:
    user_input = input("Enter study hours (0-24): ")
    test_hours = float(user_input)
    
    if 0 <= test_hours <= 24:
        score = predict_score(test_hours)
        print(f"Predicted Score for {test_hours} hours: {score}")
        
        # Risk Flag
        if score < 50:
            print("⚠️ Student may need support (Risk: Low score predicted)")
        else:
            print("✅ Student is performing well")
    else:
        print("❌ Please enter a valid number of hours between 0 and 24.")

except ValueError:
    print("❌ Invalid input. Please enter a numerical value for study hours.")

# 8. PRINT MODEL COEFFICIENTS
print("\n--- 8. Model Coefficients ---")
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope (Coefficient): {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"\nInterpretation: For every additional study hour, marks increase by approximately {slope:.2f} points.")
