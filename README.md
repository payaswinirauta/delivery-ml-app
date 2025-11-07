# 🚀 Delivery ML App

A smart **Machine Learning web app** that predicts **customer satisfaction ratings** based on shipment details — built using **FastAPI + ML Model + HTML Frontend**.

---

## 🌟 Features
- 🧠 **ML Model (Random Forest)** trained on real-world shipment data  
- ⚡ **FastAPI Backend** for fast and reliable API calls  
- 💻 **Responsive Frontend** (HTML + JS) for user interaction  
- 📊 Predicts Customer Rating instantly with real-time form inputs  
- 🔒 Fully local setup — no external API required  

---

## 🧩 Tech Stack
| Layer | Technology |
|:------|:------------|
| Machine Learning | Scikit-learn, Pandas |
| Backend | FastAPI, Uvicorn |
| Frontend | HTML, JS, CSS |
| Model Storage | Pickle (.pkl) |
| Deployment | GitHub + Render |

---

## ⚙️ How It Works
1. User fills shipment details (weight, mode, importance, on-time delivery).  
2. FastAPI sends data to ML model for prediction.  
3. Model instantly returns a ⭐ rating (1–5).  

---
```
## 📁 Project Structure
delivery-ml-app/
│
├── backend/
│ ├── train_model.py # ML model training
│ ├── main.py # FastAPI backend
│ ├── mydata.csv # Dataset
│ └── delivery_rating_model.pkl # Trained ML model
│
├── frontend/
│ └── index.html # Web interface
│
└── requirements.txt # Dependencies


---
---
```
## 🧰 Installation (Run Locally)
```bash
git clone https://github.com/payaswinirauta/delivery-ml-app.git
cd delivery-ml-app
pip install -r requirements.txt
uvicorn backend.main:app --reload
Then open 👉 frontend/index.html in your browser.

🧠 Example Prediction
Input	Output
Product Weight: 2	⭐ Predicted Rating: 4
Mode: Road	
Importance: Medium	
On-time: Yes	

💼 Author
👩‍💻 Payaswini Rauta
AI + FastAPI Developer | Machine Learning Enthusiast
🌐 GitHub Profile

⭐ If you like this project, give it a star on GitHub!

```

---

### 🔧 Next Step:
1. Go to your repo → click **“Add a README”**  
2. Paste the above content  
3. Commit changes ✅  

---

Chaaho to main is README ka **Render Live Deployment version** bhi bana du jisme “🌍 Live Demo” section add hoga (after you deploy it).  
Batao, deploy hone ke baad wo version chahiye kya?
