from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Model load karo
model = joblib.load("backend/delivery_rating_model.pkl")

app = FastAPI()

# CORS allow karo frontend ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(
    product_weight: float = Form(...),
    shipment_mode: str = Form(...),
    product_importance: str = Form(...),
    on_time_delivery: str = Form(...)
):
    # Encoding manually (same as Kaggle model)
    shipment_dict = {"Flight": 0, "Road": 1, "Ship": 2}
    importance_dict = {"Low": 0, "Medium": 1, "High": 2}
    delivery_dict = {"No": 0, "Yes": 1}

    X = [[
        product_weight,
        shipment_dict.get(shipment_mode, 0),
        importance_dict.get(product_importance, 0),
        delivery_dict.get(on_time_delivery, 0)
    ]]
    prediction = model.predict(X)[0]
    return {"predicted_rating": round(prediction, 2)}
