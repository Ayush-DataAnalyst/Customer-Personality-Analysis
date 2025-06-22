import streamlit as st
from customer_personality_analysis.pipeline.prediction_pipeline import predict_cluster

# ------------------ Page Setup ------------------
st.set_page_config(
    page_title="Customer Segmentation App 🎯",
    layout="centered",
    page_icon="🧠"
)

# ------------------ Dark Mode Toggle ------------------
mode = st.sidebar.radio("🎨 Choose Theme", ["Light", "Dark"], horizontal=True)

# Inject basic styles
if mode == "Dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
        }
        .block-container {
            background-color: rgba(33, 37, 41, 0.95);
            padding: 2rem;
            border-radius: 15px;
        }
        label, .stSlider, .stNumberInput > div > div > input {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1562813733-b31f71025d54?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .block-container {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            color: black;
        }

        label, .stSlider, .stNumberInput > div > div > input {
            color: black !important;
        }

        h1, h2, h3, h4, h5, h6, p {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# ------------------ App UI ------------------
st.title("🧩 Customer Cluster Predictor")
st.markdown("Know your customers better. Enter the details below to predict which **customer segment** they belong to.")

with st.form("cluster_form"):
    st.subheader("💼 Demographics")
    col1, col2 = st.columns(2)
    with col1:
        income = st.slider("Annual Income (USD)", 0, 200000, 50000, step=1000)
        age = st.slider("Customer Age", 18, 100, 35)
    with col2:
        spending = st.slider("🛍️ Total Spending", 0, 10000, 1500)

    st.markdown("---")
    st.subheader("🛒 Product Category Spending")
    col1, col2, col3 = st.columns(3)
    with col1:
        wines = st.slider("🍷 Wines", 0, 1000, 300)
        fruits = st.slider("🍎 Fruits", 0, 500, 50)
    with col2:
        meat = st.slider("🥩 Meat Products", 0, 1000, 300)
        fish = st.slider("🐟 Fish Products", 0, 500, 100)
    with col3:
        sweets = st.slider("🍫 Sweet Products", 0, 500, 75)
        gold = st.slider("💎 Gold Products", 0, 500, 200)

    st.subheader("🧾 Purchase Behavior")
    col1, col2, col3 = st.columns(3)
    with col1:
        deals = st.slider("💸 Deal Purchases", 0, 20, 3)
        web = st.slider("🌐 Web Purchases", 0, 20, 5)
    with col2:
        catalog = st.slider("📦 Catalog Purchases", 0, 20, 2)
        store = st.slider("🏪 Store Purchases", 0, 20, 4)
    with col3:
        visits = st.slider("📅 Web Visits/Month", 0, 20, 3)

    submitted = st.form_submit_button("🚀 Predict Cluster")

if submitted:
    customer_data = {
        "Income": income,
        "Customer_Age": age,
        "Total_Spending": spending,
        "MntWines": wines,
        "MntFruits": fruits,
        "MntMeatProducts": meat,
        "MntFishProducts": fish,
        "MntSweetProducts": sweets,
        "MntGoldProds": gold,
        "NumDealsPurchases": deals,
        "NumWebPurchases": web,
        "NumCatalogPurchases": catalog,
        "NumStorePurchases": store,
        "NumWebVisitsMonth": visits
    }

    cluster = predict_cluster(customer_data)
    st.success(f"🎉 Predicted Segment: **Cluster {cluster}**")
    st.balloons()

    personas = {
        0: "🧘‍♂️ Balanced Buyer",
        1: "💼 High-Spender",
        2: "📦 Catalogue Shopper",
        3: "🧃 Low Engagement"
    }
    st.markdown(f"### 📌 Customer Type: {personas.get(cluster, '👤 Unknown Segment')}")
