import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib
import os
from customer_personality_analysis.exception.exception_handler import AppException
from customer_personality_analysis.logger.log import logging

def train_kmeans_model(X, df, save_model_path="model/kmeans_model.pkl", save_scaler_path="model/scaler.pkl", save_clustered_csv="artifacts/clustered_customers.csv"):
    try:
        logging.info(f"📥 Training KMeans model on raw input")

        # 1. Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        logging.info("📊 Features standardized.")

        # 2. Elbow method
        inertia = []
        for k in range(2, 11):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X_scaled)
            inertia.append(kmeans.inertia_)

        # 3. Save Elbow Curve
        os.makedirs("artifacts", exist_ok=True)
        plt.figure(figsize=(8, 4))
        sns.lineplot(x=range(2, 11), y=inertia, marker="o")
        plt.title("Elbow Method - Optimal K")
        plt.xlabel("Number of clusters")
        plt.ylabel("Inertia")
        plt.savefig("artifacts/elbow_curve.png")
        plt.close()
        logging.info("📈 Elbow curve saved to: artifacts/elbow_curve.png")

        # 4. Final clustering
        optimal_k = 4
        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        df["cluster_label"] = kmeans.fit_predict(X_scaled)

        # 5. Save clustered data
        df.to_csv(save_clustered_csv, index=False)
        logging.info(f"✅ Clustered data saved to: {save_clustered_csv}")

        # 6. Save model and scaler
        os.makedirs(os.path.dirname(save_model_path), exist_ok=True)
        joblib.dump(kmeans, save_model_path)
        joblib.dump(scaler, save_scaler_path)
        logging.info(f"💾 KMeans model saved to: {save_model_path}")
        logging.info(f"💾 Scaler saved to: {save_scaler_path}")

        return df

    except Exception as e:
        raise AppException("❌ Error during model training", e)
