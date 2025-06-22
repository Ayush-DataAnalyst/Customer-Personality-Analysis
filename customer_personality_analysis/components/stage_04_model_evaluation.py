import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from customer_personality_analysis.exception.exception_handler import AppException
from customer_personality_analysis.logger.log import logging

def evaluate_clusters(clustered_csv_path="artifacts/clustered_customers.csv", save_dir="artifacts/cluster_analysis"):
    try:
        logging.info(f"📥 Loading clustered data from: {clustered_csv_path}")
        df = pd.read_csv(clustered_csv_path)

        os.makedirs(save_dir, exist_ok=True)

        # 1. Summary statistics per cluster
        cluster_summary = df.groupby("cluster_label").agg({
            'Income': ['mean', 'median'],
            'Total_Spending': ['mean', 'median'],
            'Customer_Age': ['mean', 'median'],
            'NumWebPurchases': ['mean'],
            'NumStorePurchases': ['mean']
        })
        cluster_summary.to_csv(f"{save_dir}/cluster_summary.csv")
        logging.info("📄 Cluster summary saved.")

        # 2. Visualize feature distribution per cluster
        features_to_plot = ['Income', 'Total_Spending', 'Customer_Age']
        plt.figure(figsize=(10, 5 * len(features_to_plot)))
        for i, feature in enumerate(features_to_plot):
            plt.subplot(len(features_to_plot), 1, i+1)
            sns.boxplot(data=df, x="cluster_label", y=feature, palette="Set2")
            plt.title(f"Distribution of {feature} across Clusters")

        plt.tight_layout()
        plt.savefig(f"{save_dir}/cluster_distributions.png")
        logging.info("📊 Cluster distribution plots saved.")

        # 3. Count of customers in each cluster
        cluster_counts = df["cluster_label"].value_counts().sort_index()
        plt.figure(figsize=(6, 4))
        sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette="Set3")
        plt.title("Customer Count per Cluster")
        plt.xlabel("Cluster Label")
        plt.ylabel("Number of Customers")
        plt.tight_layout()
        plt.savefig(f"{save_dir}/cluster_counts.png")
        logging.info("📈 Cluster count plot saved.")

    except Exception as e:
        raise AppException("❌ Error during model evaluation", e)
