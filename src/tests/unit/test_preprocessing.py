#src/tests/unit/test_preprocessing.py

import src.ML.preprocessing as prep
from src.tests.fixtures import *


def test_validate_data_invalid(bad_data_frame):
    with pytest.raises(ValueError):
        prep.validate_data(bad_data_frame)

def test_validate_data_valid(good_data_frame):
    prep.validate_data(good_data_frame)

def test_preprocess_catboost(good_data_frame):
    result = prep.preprocess_catboost(good_data_frame)
    assert isinstance(result, pd.DataFrame), "catboost result is not a DataFrame"

    for col in ['id', 'customerid', 'surname']:
        assert col not in result.columns

    for old_col, new_col in prep.RENAME_COLUMNS.items():
        assert new_col in result.columns