# src/ML/predictor.py

import pandas as pd
import joblib
from .preprocessing import validate_data, preprocess_xgboost, preprocess_catboost
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent.parent / 'models' / 'best_model.pkl'

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        model = joblib.load(f)
    return model

def predict(data) -> float:
    model = load_model()

    if (model.__class__.__name__ == 'XGBClassifier'):
        data = preprocess_xgboost(data)
    elif (model.__class__.__name__ == 'CatBoostClassifier'):
        data = preprocess_catboost(data)

    return model.predict_proba(data)[:, 1]