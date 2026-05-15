import pytest
import pandas as pd
import os

def test_data_columns():
    # We check if the processed file exists first
    file_path = 'data/processed/cleaned_reviews.csv'
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        expected_columns = ['review', 'rating', 'date', 'bank', 'source']
        for col in expected_columns:
            assert col in df.columns
    else:
        pytest.skip("Cleaned data file not found. Run preprocessing first.")