import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class DataPrepKit:
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
       print(data.describe())

    # 3- Handle missing values
    def handle_missing_valuse(self , action = '', strategy = ''):
        if action == 'removing':
            return self.data.dropna()
        elif action =='inputing':
            if strategy == 'mean':
                return self.data.fillna(self.data.mean(numeric_only=None))
            elif strategy == 'median':
                return self.data.fillna(self.data.median())
            elif strategy == 'mode':
                return self.data.fillna(self.data.mode().iloc[0])
            else:
                raise ValueError("Unsupported imputation strategy. Please choose from 'mean', 'median', or 'mode'.")
        else :
            raise ValueError("two functionalty is allowed removing and ")

    # 4- Categorical Data Encoding
    def encode_categorical_data(self, columns):
        return pd.get_dummies(self.data, columns=columns)

    def label_encoding(self, column):

       label_encoder = LabelEncoder()
       self.data[column + '_encoded'] = label_encoder.fit_transform(self.data[column])
       return self.data


