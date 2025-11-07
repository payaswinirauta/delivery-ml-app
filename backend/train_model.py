# backend/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib
import os

# 🔹 Check current working directory
print("Current working directory:", os.getcwd())

# 🔹 Load dataset
try:
    df = pd.read_csv("mydata.csv")  # relative path
except FileNotFoundError:
    # fallback to absolute path
    df = pd.read_csv(r"C:\Users\SAI\OneDrive\Desktop\delivery-ml-app\backend\mydata.csv")
print("✅ Dataset loaded successfully!")

# 🔹 Encode text columns to numbers
df['shipment_mode'] = df['shipment_mode'].astype('category').cat.codes
df['product_importance'] = df['product_importance'].astype('category').cat.codes
df['on_time_delivery'] = df['on_time_delivery'].map({'Yes': 1, 'No': 0})

# 🔹 Split data
X = df[['product_weight', 'shipment_mode', 'product_importance', 'on_time_delivery']]
y = df['customer_rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Train model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# 🔹 Save locally
joblib.dump(model, "backend/delivery_rating_model.pkl")
print("✅ Model trained and saved locally!")
