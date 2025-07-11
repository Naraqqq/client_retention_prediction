# src/tests/unit/test_predictor.py

import pytest
import pandas as pd
from src.ML.predictor import predict
from src.tests.fixtures import *


def test_predict_returns_float(predictor_data_frame):
    result = predict(predictor_data_frame)
    assert isinstance(result[0], float), "predciton type"
    assert 0.0 <= result[0] <= 1.0