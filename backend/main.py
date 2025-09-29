from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
import numpy as np
from utils import clean_text

# -------------------------------
# Load Models
# -------------------------------
# Logistic Regression models/vectorizers
clf1 = joblib.load("models/layer1_logreg_model.pkl")
vectorizer1 = joblib.load("models/vectorizer_layer1.pkl")
clf2 = joblib.load("models/layer2_logreg_model.pkl")
vectorizer2 = joblib.load("models/vectorizer_layer2.pkl")

# Naive Bayes models/vectorizers
nb_clf1 = joblib.load("models/layer1_nb_model.pkl")
nb_vectorizer1 = joblib.load("models/vectorizer_layer1_nb.pkl")
nb_clf2 = joblib.load("models/layer2_nb_model.pkl")
nb_vectorizer2 = joblib.load("models/vectorizer_layer2_nb.pkl")

# Hybrid voting weights (configurable via env)
W_LR = float(os.getenv("HYBRID_W_LR", 0.5))
W_NB = 1.0 - W_LR

# -------------------------------
# Initialize FastAPI
# -------------------------------
app = FastAPI(title="Spam Detection API")

# -------------------------------
# Enable CORS
# -------------------------------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
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

    # -------------------------------
    # Layer 1: Spam/Ham classification
    # -------------------------------
    X_lr1 = vectorizer1.transform([msg_clean])
    X_nb1 = nb_vectorizer1.transform([msg_clean])

    spam_idx_lr1 = list(clf1.classes_).index(1) if 1 in set(clf1.classes_) else 0
    spam_idx_nb1 = list(nb_clf1.classes_).index(1) if 1 in set(nb_clf1.classes_) else 0

    p_lr1 = clf1.predict_proba(X_lr1)[:, spam_idx_lr1]
    p_nb1 = nb_clf1.predict_proba(X_nb1)[:, spam_idx_nb1]

    p_ens1 = W_LR * p_lr1 + W_NB * p_nb1
    is_spam = bool((p_ens1 >= 0.5)[0])

    if not is_spam:
        return {"label": "Ham", "confidence": "Safe Email"}

    # -------------------------------
    # Layer 2: Spam type classification
    # -------------------------------
    X_lr2 = vectorizer2.transform([msg_clean])
    X_nb2 = nb_vectorizer2.transform([msg_clean])

    proba_lr2 = clf2.predict_proba(X_lr2)[0]
    proba_nb2 = nb_clf2.predict_proba(X_nb2)[0]

    classes_lr2 = list(clf2.classes_)
    classes_nb2 = list(nb_clf2.classes_)

    # Reorder NB probabilities to match LR classes and convert to np.array
    reordered_nb2 = np.array([proba_nb2[classes_nb2.index(c)] for c in classes_lr2])

    # Ensemble probability (element-wise multiplication works with np.array)
    proba_ens2 = W_LR * proba_lr2 + W_NB * reordered_nb2

    spam_type = classes_lr2[int(proba_ens2.argmax())]

    return {"label": "Spam", "spam_type": spam_type, "confidence": "High Posibility"}

@app.get("/stats")
def get_dataset_stats():
    """Return dataset statistics for visualization"""
    return {
        "total_emails": 517401,
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
        "algorithm": "Logistic Regression + Naive Bayes Hybrid (Two-Layer)",
        "training_data_size": "517,401 emails",
        "feature_vector_size": 3000
    }
