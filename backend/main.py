from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from utils import clean_text

# -------------------------------
# Load Models
# -------------------------------
clf1 = joblib.load("models/layer1_logreg_model.pkl")
vectorizer1 = joblib.load("models/vectorizer_layer1.pkl")
clf2 = joblib.load("models/layer2_logreg_model.pkl")
vectorizer2 = joblib.load("models/vectorizer_layer2.pkl")

# -------------------------------
# Initialize FastAPI
# -------------------------------
app = FastAPI(title="Spam Detection API")

# -------------------------------
# Enable CORS
# -------------------------------
origins = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],
)

# -------------------------------
# Request model
# -------------------------------
class EmailRequest(BaseModel):
    message: str

# -------------------------------
# Endpoints
# -------------------------------
@app.get("/")
def root():
    return {"message": "Spam Detection API is running."}

@app.post("/predict")
def predict_email(req: EmailRequest):
    msg_clean = clean_text(req.message)
    X_input1 = vectorizer1.transform([msg_clean])
    label = clf1.predict(X_input1)[0]


    if label == 0:
        return {"label": "Ham", "confidence": "Safe Email"}
    else:
        X_input2 = vectorizer2.transform([msg_clean])
        spam_type = clf2.predict(X_input2)[0]
        return {"label": "Spam", "spam_type": spam_type, "confidence": "High Risk"}

@app.get("/stats")
def get_dataset_stats():
    """Return dataset statistics for visualization"""
    return {
        "total_emails": 517401,  # 312770 + 204631
        "spam_count": 204631,
        "ham_count": 312770,
        "model_performance": {
            "accuracy": 96.58,
            "precision": 98.41,
            "recall": 92.86,
            "f1_score": 95.55
        },
        "features_used": [
            "text_length",
            "word_count", 
            "punctuation_count",
            "uppercase_ratio",
            "digit_count",
            "url_count"
        ],
        "algorithm": "Logistic Regression (Two-Layer)",
        "training_data_size": "517,401 emails",
        "feature_vector_size": 3000
    }
