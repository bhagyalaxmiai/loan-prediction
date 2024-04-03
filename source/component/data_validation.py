import pandas as pd
import numpy as np
from source.exception import LoanException

class DataValidation:
    def __init__(self, utility_config):
        self.utility_config = utility_config


    def handle_missing_value(self, data, type):
        try:
            if type == 'train':
                numerical_columns = data.select_dtypes(include=['number']).columns
                numerical_imputation_values = data[numerical_columns].median()
                data[numerical_columns] = data[numerical_columns].fillna(numerical_imputation_values)

                categorical_columns = data.select_dtypes(include=['object']).columns
                categorical_imputation_values = data[categorical_columns].mode().iloc[0]
                data[categorical_columns] = data[categorical_columns].fillna(categorical_imputation_values)

                imputation_values = pd.concat([numerical_imputation_values,categorical_imputation_values])
                imputation_values.to_csv(self.utility_config.imputation_values_file, header=['Imputation_Value'])
            else:
                imputation_values = pd.read_csv(self.utility_config.imputation_values_file, index_col=0)['Imputation_Value']

                numerical_columns = data.select_dtypes(include=['number']).columns
                data[numerical_columns] = data[numerical_columns].fillna(imputation_values[numerical_columns])

                categorical_columns = data.select_dtypes(include=['object']).columns
                data[categorical_columns] = data[categorical_columns].fillna(imputation_values[categorical_columns])

            return data
        except LoanException as e:
            raise e

    def initiate_data_validation(self):
        train_data = pd.read_csv(self.utility_config.train_file_path, dtype={'Credit_History':'object', 'ApplicantIncome':'float64'})
        test_data = pd.read_csv(self.utility_config.test_file_path, dtype={'Credit_History':'object', 'ApplicantIncome':'float64'})
        train_data = self.handle_missing_value(train_data, type='train')
        test_data = self.handle_missing_value(test_data, type='test')

        # train_data.to_csv('train_data_Processed.csv', index=False)
        # test_data.to_csv('test_data_Processed.csv', index=False)
        print("DV done")
