# src/api/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.ML.predictor import predict
from src.database.crud import getCustomer, savePrediction
import json
import os

router = APIRouter()

@router.post("/predict-retention/")
def predict_retention(customerid : float, db : Session = Depends(get_db)):
    df = getCustomer(customerid, db)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(BASE_DIR, '../../models/best_treshold.json')

    with open(json_path, 'r') as f:
        threshold = json.load(f)

    if df is None or df.empty:
        raise HTTPException(status_code=404, detail="Customer not found or no data available")

    prediction = float(predict(df))
    savePrediction(customerid, prediction, db)
    message = ("АХТУНГ КЛИЕНТ УТЕКАЕТ НЕМЕДЛЕННО ДАТЬ КОШКОЖЕНА"
               if prediction > threshold else "ЭТОТ ПУПСИК С НАМИ ДОИМ ДАЛЬШЕ")

    if prediction is None:
        return None
    else:
        return {'customerid' : customerid,
                'prediction' : prediction,
                'message' : message}