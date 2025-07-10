# src/database/crud.py

import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import text



def getCustomer(customerid : float, db : Session):
    df = pd.read_sql(text("SELECT * FROM churn_customers WHERE customerid = :customerid"),
                     con=db.bind,
                     params={'customerid': customerid})

    return df

def savePrediction(customerid : float, prediction : float, db : Session):
    db.execute(text("INSERT INTO retention_proba (customerid, retentionproba) VALUES (:customerid, :prediction)"),
               {'customerid': customerid, 'prediction': prediction})
    db.commit()