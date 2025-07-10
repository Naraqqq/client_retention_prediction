# src/ML/preprocessing.py

import pandas as pd
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

COLUMNS = ['id', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender',
       'Age', 'Tenure', 'Balance', 'Num_Of_Products', 'Has_Cr_Card',
       'Is_Active_Member', 'Estimated_Salary']
COLUMNS = [col.lower() for col in COLUMNS]

RENAME_COLUMNS = {
    'creditscore': 'CreditScore',
    'geography': 'Geography',
    'gender': 'Gender',
    'age': 'Age',
    'tenure': 'Tenure',
    'balance': 'Balance',
    'num_of_products': 'NumOfProducts',
    'has_cr_card': 'HasCrCard',
    'is_active_member': 'IsActiveMember',
    'estimated_salary': 'EstimatedSalary'
}

def validate_data(data: pd.DataFrame):
    missed_columns = [col for col in COLUMNS if col not in data.columns]
    if missed_columns:
        raise ValueError(f"Missing columns: {missed_columns}")

def preprocess_xgboost(data: pd.DataFrame) -> pd.DataFrame:
    processed_data = pd.get_dummies(data)

    return processed_data

def preprocess_catboost(data: pd.DataFrame) -> pd.DataFrame:
    data_drop = data.drop(columns = ['id', 'customerid', 'surname'])
    data_drop = data_drop.rename(columns=RENAME_COLUMNS)
    return data_drop
