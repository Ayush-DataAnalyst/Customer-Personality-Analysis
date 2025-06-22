import pandas as pd
import os
import yaml
from customer_personality_analysis.logger.log import log
from customer_personality_analysis.exception.exception_handler import AppException

def read_params(config_path="config/config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config

def load_data():
    try:
        config = read_params()
        source_path = config["data_ingestion"]["source_file"]
        output_path = config["data_ingestion"]["output_file"]

        print(f"🔍 Trying to read Excel file from: {source_path}")
        df = pd.read_excel(source_path)  # likely failure point

        print(f"📁 Saving cleaned CSV to: {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)

        log(f"✅ Data loaded and saved successfully.")
        return df

    except FileNotFoundError as fe:
        print(f"❌ FileNotFoundError: {fe}")
        raise AppException("File not found", fe)

    except Exception as e:
        print(f"❌ Exception occurred in load_data(): {e}")
        raise AppException("Error in data ingestion", e)
