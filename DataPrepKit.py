import numpy as np
import pandas as pd


class DataPrep:
    def __init__(self, data):
        self.data = data
        super().__init__()

     #1- read data
    def read_data(data_path):
        if data_path.endswith("csv"):
            data = pd.read_csv(data_path)
        elif data_path.endswith("xlsx"):
            data = pd.read_excel(data_path)
        elif data_path.endswith("json"):
            data = pd.read_json(data_path)
        else:
                raise ValueError("Unsupported file format. Only CSV, Excel, and JSON are supported.")
        return data

    # 2- data summary
    # def data_summary(self):
    #     summary = {}
    #     summary['mean'] = self.data.mean()
    #     summary['median'] = self.data.median()
    #     summary['mode'] = self.data.mode().iloc[0]  # Mode might return multiple values
    #     summary['std_dev'] = self.data.std()
    #     return summary

    def summary(self):
       print(self.data.describe())

    # 3- Handle missing values
    def handle_missing_valuse(self , action = '', strategy = ''):
        column_names = self.columns.tolist()
        df = self.data
        df_copy = df.copy()

        if action == 'removing':
            return self.data.dropna()
       
        elif action =='inputing':
             for col in column_names:
                if df_copy[col].dtype == 'object':  # Categorical column
                     mode_val = df_copy[col].mode()[0]  
                     df_copy[col].fillna(mode_val, inplace=True)  # Replace missing values with the mode
              
                 # Numeric columns
             if strategy == 'mean':
                  df_copy.fillna(df_copy.mean()) 
             elif strategy == 'median':
                  df_copy.fillna(df_copy.median())
             elif strategy == 'mode':
                  df_copy.fillna(df_copy.mode().iloc[0])
             else:
                 raise ValueError("Unsupported imputation strategy. Please choose from 'mean', 'median', or 'mode'.")
        else :
            raise ValueError("two functionalty is allowed removing and ")
        
        return df_copy
    # 4- Categorical Data Encoding
    def encode_categorical_data(self, columns):
        return pd.get_dummies(self.data, columns=columns)

   


