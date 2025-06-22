import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from customer_personality_analysis.exception.exception_handler import AppException
from customer_personality_analysis.logger.log import logging

def transform_data(cleaned_data_path="D:/Customer Personality Analysis Project/cleaned_data.csv"):
    try:
        logging.info(f"📂 Loading cleaned data from: {cleaned_data_path}")
        df = pd.read_csv(cleaned_data_path)

        features = [
            'Income', 'Customer_Age', 'Total_Spending',
            'MntWines', 'MntFruits', 'MntMeatProducts',
            'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
            'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
            'NumStorePurchases', 'NumWebVisitsMonth'
        ]

        X = df[features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # ✅ Make sure the artifacts folder exists before saving
        os.makedirs("artifacts", exist_ok=True)

        # ✅ Save transformed data to file
        pd.DataFrame(X_scaled, columns=features).to_csv("artifacts/transformed_data.csv", index=False)
        logging.info("✅ Data transformation completed and saved to artifacts/transformed_data.csv")

        return X_scaled, df, X  # Return original (unscaled) features too


    except Exception as e:
        raise AppException("❌ Error during data transformation", e)
