import os
import pandas as pd
import numpy as np
from source.exception import LoanException
from source.logger import logging

class DataValidation:
    def __init__(self, utility_config):
        self.utility_config = utility_config
        self.outlier_params = {}


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
                data[categorical_columns] = data[categorical_columns].fillna(imputation_values[categorical_columns].iloc[0])

            return data
        except LoanException as e:
            raise e


    def export_data_file(self,data,file_name, path):
        try:
            dir_path = os.path.join(path)
            os.makedirs(dir_path, exist_ok=True)

            data.to_csv(path + '\\' + file_name, index=False)

            logging.info('Data validation files exported')


        except LoanException as e:
            raise e


    def outlier_detection_handle(self,data, type):
        try:
            if type=='train':

                for column_name in data.select_dtypes(include=['number']).columns:
                    Q1 = data[column_name].quantile(0.25)
                    Q3 = data[column_name].quantile(0.75)

                    IQR = Q3 - Q1

                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR

                    self.outlier_params[column_name] = {'Q1' : Q1, 'Q3': Q3, 'IQR': IQR}

                    outlier_mask = (data[column_name] < lower_bound) | (data[column_name] > upper_bound)

                    data.loc[outlier_mask, column_name] = np.log1p(data.loc[outlier_mask, column_name])

                outlier_params_df = pd.DataFrame(self.outlier_params)
                outlier_params_df.to_csv(self.utility_config.outliers_params_file, index=False)

            else:
                outlier_params_df = pd.read_csv(self.utility_config.outliers_params_file)
                self.outlier_params = outlier_params_df.to_dict(orient='list')

                for column_name in data.select_dtypes(include=['number']).columns:
                    if column_name in self.outlier_params:

                        Q1 = self.outlier_params[column_name][0]
                        Q3 = self.outlier_params[column_name][1]
                        IQR = self.outlier_params[column_name][2]

                        lower_bound = Q1 - 1.5 * IQR
                        upper_bound = Q3 + 1.5 * IQR

                        outlier_mask = (data[column_name] < lower_bound) | (data[column_name] > upper_bound)

                        data.loc[column_name] = np.log1p(data.loc[outlier_mask, column_name])

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

        train_data = self.outlier_detection_handle(train_data, type='train')
        test_data = self.outlier_detection_handle(test_data, type='test')

        self.export_data_file(train_data, self.utility_config.train_file_name, self.utility_config.dv_train_file_path)
        self.export_data_file(test_data,  self.utility_config.test_file_name, self.utility_config.dv_test_file_path)


        print("DV done")
