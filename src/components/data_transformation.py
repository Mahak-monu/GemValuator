# Importing necessary libraries
from sklearn.impute import SimpleImputer           # Handles missing values
from sklearn.preprocessing import StandardScaler   # Scales numeric features
from sklearn.preprocessing import OrdinalEncoder   # Encodes categorical features
from sklearn.pipeline import Pipeline              # Builds pipelines
from sklearn.compose import ColumnTransformer      # Applies transformations to specific columns

import sys, os
from dataclasses import dataclass
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

# Configuration for storing preprocessor object file
@dataclass
class DataTransformationconfig:
    preprocessor_ob_file_path = os.path.join('artifacts', 'preprocessor.pkl')


# Data transformation class
class DataTransformation:
    def __init__(self):
        # Set configuration path
        self.data_transformation_config = DataTransformationconfig()

    # This function creates and returns the preprocessing object
    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')

            # Define which columns are categorical and which are numerical
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Specify the category order for encoding (Ordinal Encoding)
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

            logging.info('Pipeline Initiated')

            # Numerical pipeline: fill missing with median and scale values
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Categorical pipeline: fill missing with most frequent and encode, then scale
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                ('scaler', StandardScaler())
            ])

            # Combine pipelines using ColumnTransformer
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])

            return preprocessor

        except Exception as e:
            logging.info('Error in Data Transformation')
            raise CustomException(e, sys)

    # This function will be used to apply the transformation on train and test data and returns transformned arrays
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('read train and test data completed')
            logging.info(f'Train Dataframe head : \n{train_df.head().to_string()}')
            logging.info(f'Test DataFrame Head : \n{test_df.head().to_string()}')

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']

            ## features into independent and dependent features

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name, 'id'], axis = 1)
            target_feature_test_df = test_df[target_column_name]

            # apply the transformation
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets")

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            ## save object function calling
            save_object(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj = preprocessing_obj
            )

            logging.info("preprocessor pickle is created and saved")

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path
            )
        

        except Exception as e:
            logging.info("Error occured in initiate data transformation")

            raise CustomException(e, sys)










# 📘 Easy Explanation (Like a Story)
# Let’s imagine you are preparing gemstone data for a machine learning model.

# You have a dataset containing:

# Numeric values (e.g. carat size, dimensions like x, y, z)

# Categorical values (e.g. clarity, cut, color)

# To make this data usable for a model, you need to clean it, fill missing values, and convert text labels into numbers, because machines don’t understand text!

# Here’s what happens in this code:

# Define where to save things
# A file called preprocessor.pkl will be saved inside the artifacts folder — this file contains all the preprocessing steps so they can be reused.

# Create preprocessing pipelines:

# For numerical columns:

# Fill any missing values with the median

# Then scale them (so all numbers are on the same range)

# For categorical columns:

# Fill missing values with the most frequent value

# Convert categories to numbers in a meaningful order (e.g. clarity from low to high)

# Scale them too

# Combine both pipelines:
# Using ColumnTransformer, we make one big machine that applies the correct transformation to the correct type of column.

# Return this preprocessor:
# This object is ready to be used later to transform the actual data.