import os
from pathlib import Path
import logging

# Configure logging to provide timestamps and informational messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# Define the name of the root project folder
project_name = "customer_personality_analysis"


# List of files and directories to create for the project structure
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/stage_00_data_ingestion.py",
    f"{project_name}/components/stage_01_data_validation.py",
    f"{project_name}/components/stage_02_data_transformation.py",
    f"{project_name}/components/stage_03_model_trainer.py", # This could be for clustering or classification
    f"{project_name}/components/stage_04_model_evaluation.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception_handler.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/log.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/util.py",
    "notebooks/exploratory_data_analysis.ipynb", # A common place for EDA notebooks
    "config/config.yaml",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]


# Loop through the list of file paths to create the structure
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")