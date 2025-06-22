import pandas as pd
import yaml
from customer_personality_analysis.logger.log import log
from customer_personality_analysis.exception.exception_handler import AppException

def read_params(config_path="config/config.yaml"):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def validate_data():
    try:
        config = read_params()
        cleaned_data_path = config["data_cleaning"]["cleaned_data_path"]
        expected_columns = config["data_validation"]["expected_columns"]

        log(f"📂 Reading cleaned data from: {cleaned_data_path}")
        df = pd.read_csv(cleaned_data_path)

        # ✅ Check 1: Missing values
        if df.isnull().sum().sum() > 0:
            raise AppException("❌ Data contains missing values", "Nulls found")

        # ✅ Check 2: Column names match
        if sorted(df.columns.tolist()) != sorted(expected_columns):
            raise AppException("❌ Data columns mismatch", f"Expected: {expected_columns}, Found: {df.columns.tolist()}")

        log("✅ Data validation passed: No missing values and all expected columns are present.")
        return True

    except Exception as e:
        log(f"❌ Data validation failed: {e}")
        raise AppException("Data validation failed", e)
