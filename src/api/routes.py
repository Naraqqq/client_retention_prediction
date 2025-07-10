# src/api/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.ML.predictor import predict
from src.database.crud import getCustomer, savePrediction


router = APIRouter()

@router.post("/predict-retention/")
def predict_retention(customerid : float, db : Session = Depends(get_db)):
    df = getCustomer(customerid, db)
    prediction = float(predict(df))
    savePrediction(customerid, prediction, db)

    if prediction is None:
        return None
    else:
        return {'customerid' : customerid,
                'prediction' : prediction}