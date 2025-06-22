from customer_personality_analysis.pipeline.prediction_pipeline import predict_cluster

# Example new customer data
customer = {
    'Income': 60000,
    'Customer_Age': 35,
    'Total_Spending': 1500,
    'MntWines': 500,
    'MntFruits': 50,
    'MntMeatProducts': 300,
    'MntFishProducts': 100,
    'MntSweetProducts': 75,
    'MntGoldProds': 200,
    'NumDealsPurchases': 2,
    'NumWebPurchases': 5,
    'NumCatalogPurchases': 1,
    'NumStorePurchases': 4,
    'NumWebVisitsMonth': 3
}

cluster = predict_cluster(customer)
print(f"Predicted cluster: {cluster}")
