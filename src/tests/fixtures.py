#src/tests/unit/fixtures.py

import pytest
import pandas as pd

COLUMNS_FOR_MODEL = {
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

COLUMNS = ['id', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender',
       'Age', 'Tenure', 'Balance', 'Num_Of_Products', 'Has_Cr_Card',
       'Is_Active_Member', 'Estimated_Salary']
COLUMNS = [col.lower() for col in COLUMNS]


@pytest.fixture
def bad_data_frame():
    return pd.DataFrame(columns=['AGE', 'GENDER'], data = [[23, 'female']])

@pytest.fixture
def good_data_frame():
    return pd.DataFrame(columns=COLUMNS, data=[[1, 'Germany', 'male',
                                                                  30, 2, 100000,
                                                                  2, 1, 1, 99999,
                                                11, 12, 13]])


@pytest.fixture
def predictor_data_frame():
    return pd.DataFrame([{
        'id': 11,
        'customerid' : 12312,
        'surname' : "32432",
        'CreditScore': 600,
        'Geography': 'France',
        'Gender': 'Male',
        'Age': 40,
        'Tenure': 3,
        'Balance': 60000,
        'NumOfProducts': 2,
        'HasCrCard': 1,
        'IsActiveMember': 1,
        'EstimatedSalary': 50000
    }])