# 🧠 Customer Personality Analysis with Streamlit Deployment

Welcome to the **Customer Personality Analysis** project! This project performs in-depth clustering on marketing campaign data to uncover distinct customer segments. The end goal is to empower businesses to target and serve their customers more effectively.

<div align="center">
  <img src="https://images.unsplash.com/photo-1625535069654-cfeb8f829088?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"/>
</div>

---

## 🚀 Live App

👉 [Try the Streamlit App Here](https://customer-personality-analysis-ttkerkaphpwatgzpaeydvp.streamlit.app/)

---

## 🧩 Project Overview

**Customer Personality Analysis** is a machine learning pipeline to segment customers based on demographics, product preferences, and shopping behavior using unsupervised clustering (KMeans). This enables businesses to:

* Understand **who** their customers are
* Identify **which** segments are more profitable
* Optimize marketing campaigns and product offerings

---

## 📊 Features

* 🧼 Data cleaning & preprocessing
* 🔍 EDA (Exploratory Data Analysis)
* ⚖ Feature scaling (StandardScaler)
* 🔢 KMeans Clustering (with Elbow Method)
* 💾 Model & Scaler Persistence with `joblib`
* 🔮 Real-time Single & Batch Prediction
* 🌐 Interactive Streamlit App
* 🌗 Dark & Light Mode Switch
* 🎨 Custom UI with emojis, sliders, and backgrounds

---

## 🏗 Project Architecture

```
Customer-Personality-Analysis/
|
├── artifacts/                   # Elbow curve, clustered CSV
├── model/                       # Trained KMeans model & scaler
├── customer_personality_analysis/
│   ├── components/              # Data transformer & trainer
│   ├── pipeline/                # Prediction logic
│   ├── exception/               # Custom exceptions
│   └── logger/                  # Logging utility
│
├── app.py                       # Streamlit application
├── requirements.txt             # Required libraries
├── Dockerfile                   # Docker setup
├── .dockerignore                # Docker ignore rules
└── README.md                    # You are here ✅
```

---

## 📁 Dataset Overview

The dataset contains information about **customer demographics, purchasing behavior**, and **marketing campaign responses**.

### Key Columns:

* **Demographics**: `Income`, `Customer_Age`, `Education`, `Marital_Status`
* **Purchasing**: `MntWines`, `MntMeatProducts`, `NumWebPurchases`, etc.
* **Engagement**: `Recency`, `NumWebVisitsMonth`, `Complain`, `Response`

---

## 🧪 How to Run Locally

```bash
# Clone the repository
$ git clone https://github.com/Ayush-DataAnalyst/Customer-Personality-Analysis.git
$ cd Customer-Personality-Analysis

# Create virtual environment & activate
$ conda create -n customer_personality python=3.10
$ conda activate customer_personality

# Install dependencies
$ pip install -r requirements.txt

# Run the Streamlit app
$ streamlit run app.py
```

---

## 🐳 Run with Docker

```bash
# Build Docker Image
$ docker build -t customer-personality-app .

# Run Container
$ docker run -p 8501:8501 customer-personality-app
```

---

## ✨ Sample UI Preview

![Streamlit Demo](https://github.com/Ayush-DataAnalyst/Customer-Personality-Analysis/assets/preview-ui.jpg)

---

## 📦 Model Inference

```python
from customer_personality_analysis.pipeline.prediction_pipeline import predict_cluster

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

print(predict_cluster(customer))
```

---

## 🎯 Clusters Breakdown (Sample Personas)

| Cluster | Label             | Description                         |
| ------- | ----------------- | ----------------------------------- |
| 0       | 🧘 Balanced Buyer | Moderate spender, steady engagement |
| 1       | 💼 High-Spender   | Buys premium products frequently    |
| 2       | 📦 Catalogue Fan  | Loves catalog deals                 |
| 3       | 🧃 Low Engager    | Rarely buys, minimal interaction    |

---

## 📌 Future Scope

* 📤 Upload customer CSV for bulk prediction
* 📊 Cluster profiling dashboard
* 🧠 Try different clustering models (DBSCAN, GMM)
* 📍 Location-based segmentation (if data available)

---

## 🤝 Let's Connect

> Made with ❤️ by [Ayush K Sonawane](https://github.com/Ayush-DataAnalyst)

Feel free to ⭐ this repo, fork it, or suggest improvements. Happy Clustering!
