from customer_personality_analysis.components.stage_00_data_ingestion import load_data
from customer_personality_analysis.components.stage_01_data_validation import validate_data
from customer_personality_analysis.components.stage_02_data_transformation import transform_data
from customer_personality_analysis.components.stage_03_model_trainer import train_kmeans_model
from customer_personality_analysis.components.stage_04_model_evaluation import evaluate_clusters

def run_training():
    print("🚀 Starting training pipeline...")

    # Step 1: Load raw data from Excel
    df_raw = load_data()

    # Step 2: Validate cleaned CSV data
    validation_passed = validate_data()
    if not validation_passed:
        raise Exception("❌ Validation failed. Exiting pipeline.")

    # Step 3: Transform data
    X_scaled, df_clean, X_raw = transform_data()

    # Step 4: Train clustering model

    train_kmeans_model(X_raw, df_clean)  # X_raw is unscaled

    # Step 5: Evaluate model
    evaluate_clusters()


    print("✅ Training pipeline completed.")

if __name__ == "__main__":
    run_training()

