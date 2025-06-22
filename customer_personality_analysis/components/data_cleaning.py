import pandas as pd
import numpy as np
import os
import yaml
from customer_personality_analysis.logger.log import log
from customer_personality_analysis.exception.exception_handler import AppException

def read_params(config_path="config/config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config

def clean_data():
    try:
        config = read_params()
        input_path = config["data_ingestion"]["output_file"]
        output_path = config["data_cleaning"]["cleaned_data_path"]

        log(f"📥 Reading data from: {input_path}")
        df = pd.read_csv(input_path)

        # Drop useless columns if present
        df.drop(columns=["ID", "Z_CostContact", "Z_Revenue"], inplace=True, errors='ignore')

        # Convert 'Dt_Customer' to datetime
        df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

        # Create new features
        df['Customer_Age'] = 2025 - df['Year_Birth']
        df['Total_Spending'] = df[['MntWines', 'MntFruits', 'MntMeatProducts',
                                   'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

        # Drop rows with missing values
        df.dropna(inplace=True)

        # Save cleaned data
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)

        log(f"✅ Cleaned data saved to: {output_path}")
        return df

    except Exception as e:
        log(f"❌ Error in data cleaning: {e}")
        raise AppException("Error in data cleaning", e)
