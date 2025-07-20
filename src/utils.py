# 📦 Importing necessary libraries
import os          # For creating directories and handling file paths
import sys         # To fetch system-specific info (like error traceback)
import pickle      # To save/load Python objects to/from files

import numpy as np # Used commonly in ML projects (not directly used here though)
import pandas as pd # Same as above; imported for general utility
from sklearn.metrics import r2_score

# 🛠️ Custom exception and logging modules from your project
from src.exception import CustomException
from src.logger import logging

# ✅ Function to save any Python object (like model, preprocessor, etc.) to a file using pickle
def save_object(file_path, obj):
    try:
        # Step 1: Extract the folder name from the full file path
        # Example: if file_path = "artifacts/preprocessor.pkl", dir_path = "artifacts"
        dir_path = os.path.dirname(file_path)

        # Step 2: Make sure that directory exists; create it if it doesn’t
        os.makedirs(dir_path, exist_ok=True)

        # Step 3: Open the file in binary write mode
        with open(file_path, "wb") as file_obj:
            # Step 4: Save the Python object into that file using pickle
            pickle.dump(obj, file_obj)

    except Exception as e:
        # If any error occurs during saving, raise a custom exception
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train)

                 # Predict Testing data
            y_test_pred = model.predict(X_test)

            # Get R2 scores for train and test data
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        return report
        
    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info('Exception occured in load_object function utils')
        raise CustomException(e,sys)




