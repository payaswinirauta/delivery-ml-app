from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import joblib
import os

app = FastAPI()

# ✅ Safe model loading
try:
    model_path = os.path.join(os.path.dirname(__file__), "delivery_rating_model.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    model = joblib.load(model_path)
except Exception as e:
    model = None
    print(f"❌ Model load error: {e}")

# ✅ CORS settings
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
    if model is None:
        return {"error": "Model not loaded on server. Please check deployment."}

    try:
        # ✅ Manual encoding (same as training)
        shipment_dict = {"Air": 0, "Flight": 0, "Road": 1, "Ship": 2}
        importance_dict = {"Low": 0, "Medium": 1, "High": 2}
        delivery_dict = {"No": 0, "Yes": 1}

        X = [[
            product_weight,
            shipment_dict.get(shipment_mode, 0),
            importance_dict.get(product_importance, 0),
            delivery_dict.get(on_time_delivery, 0)
        ]]

        prediction = model.predict(X)[0]
        return {"predicted_rating": round(float(prediction), 2)}
    
    except Exception as e:
        return {"error": str(e)}



