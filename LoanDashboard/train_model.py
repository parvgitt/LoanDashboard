import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load data
data = pd.read_csv("loan_data.csv")

# Features and target
X = data[[
    "Age", "Loan Amount Requested", "Loan Repayment History",
    "Monthly Income", "Monthly Expenditure", "Other Loans"
]]
y = data["Loan Eligibility"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model
import os
os.makedirs("model", exist_ok=True)  # Create 'model' directory if not exists
with open("model/loan_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model saved as 'loan_model.pkl'.")
