import os  # to work with file paths and directories
import sys  # to handle system-specific parameters and exceptions
from dataclasses import dataclass  # to create a simple config class
import pandas as pd  # for handling CSV files and dataframes
from sklearn.model_selection import train_test_split  # to split data into train and test sets
from src.logger import logging  # to log progress and messages
from src.exception import CustomException  # custom error handling

#  Step 1: Define a config class to store paths where data will be saved
@dataclass
class DataIngestionconfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # path to save training data
    test_data_path: str = os.path.join('artifacts', 'test.csv')    # path to save testing data
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')      # path to save original raw data

#  Step 2: Create the DataIngestion class that does the actual data loading and splitting
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()  # load the config with paths

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")  # log that ingestion started

        try:
            # Step 3: Load the dataset from the given CSV file
            df = pd.read_csv(os.path.join('notebook', 'data', 'gemstone.csv'))
            logging.info("Dataset read as pandas dataframe")

            # Step 4: Create directory for saving artifacts if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Step 5: Save the original (raw) dataset to raw.csv
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Step 6: Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)
            logging.info("Train Test Split Done")

            # Step 7: Save the train and test data into respective files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            # Step 8: Return the file paths so they can be used in the next steps
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Step 9: If there is any error, log it and raise a custom exception
            logging.info("Exception occurred at Data Ingestion stage")
            raise CustomException(e, sys)


# Summary of What This Code Does:
# Step	Action
# ✅ 1	Reads gemstone.csv from notebooks/data/
# ✅ 2	Creates a folder called artifacts/ if it doesn't exist
# ✅ 3	Saves the original data to artifacts/raw.csv
# ✅ 4	Splits data into 70% training and 30% testing
# ✅ 5	Saves train.csv and test.csv inside artifacts/
# ✅ 6	Logs each step and handles errors cleanly