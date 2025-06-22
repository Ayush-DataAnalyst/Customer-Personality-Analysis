import pandas as pd
import joblib
from customer_personality_analysis.logger.log import logging
from customer_personality_analysis.exception.exception_handler import AppException

def predict_cluster(customer_data_dict, model_path="model/kmeans_model.pkl", scaler_path="model/scaler.pkl"):
    try:
        logging.info("📦 Loading the trained KMeans model and scaler...")
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)

        # Convert dict to DataFrame
        input_df = pd.DataFrame([customer_data_dict])

        # Define the same features as used in training (order matters!)
        features = [
            'Income', 'Customer_Age', 'Total_Spending',
            'MntWines', 'MntFruits', 'MntMeatProducts',
            'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
            'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
            'NumStorePurchases', 'NumWebVisitsMonth'
        ]

        # Standardize input
        scaled_input = scaler.transform(input_df[features])

        # Predict cluster
        cluster_label = model.predict(scaled_input)[0]
        logging.info(f"🔍 Predicted cluster: {cluster_label}")
        return cluster_label

    except Exception as e:
        raise AppException("❌ Error during prediction", e)
    
