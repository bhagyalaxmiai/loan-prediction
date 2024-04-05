# common constants
import certifi

ca = certifi.where()

TARGET_COLUMN = 'Loan_Status'
TRAIN_PIPELINE_NAME = 'training_pipeline'
ARTIFACT_DIR = 'artifact'
FILE_NAME = 'loan-train-data.csv'

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

MONGODB_URL_KEY = 'mongodb+srv://veenagabnave:aa5xcuda8yrgb6Zd@cluster0.otxvmcd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsCAFile=' + ca
DATABASE_NAME = 'loan-prediction'

# Data Ingestion Constants
DI_COLLECTION_NAME = 'loan-train-data'
DI_DIR_NAME = 'data_ingestion'
DI_FEATURE_STORE_DIR = 'feature_store'
DI_INGESTED_DIR = 'ingested'
DI_TRAIN_TEST_SPLIT_RATIO = 0.2

DI_MANDATORY_COLUMN_LIST = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History',
                         'Property_Area', 'Loan_Status', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                         'Loan_Amount_Term']

DI_MANDATORY_COLUMN_DATA_TYPE = {'Gender': 'object', 'Married': 'object', 'Dependents': 'object', 'Education': 'object',
                              'Self_Employed': 'object', 'Credit_History': 'object', 'Property_Area': 'object',
                              'Loan_Status': 'object', 'ApplicantIncome': 'float64', 'CoapplicantIncome': 'float64',
                              'LoanAmount': 'float64', 'Loan_Amount_Term': 'float64'}

# Data Validation Constants
DV_IMPUTATION_VALUES_FILE = "source/ml/imputation_values.csv"
DV_OUTLIERS_PARAMS_FILE = "source/ml/outliers_details.csv"
DV_DIR_NAME = 'data_validation'


# Data transformation constant
DT_MULTI_CLASS_COL = ['Dependents', 'Property_Area']
DT_BINARY_CLASS_COL = ['Gender', 'Married', 'Education', 'Self_Employed']
DT_ENCODER_PATH = 'source/ml/multi_class_encoder.pkl'
DT_DIR_NAME: str = "data_transformation"

# model train and evaluate

MODEL_PATH = "source/ml/artifact"
FINAL_MODEL_PATH = "source/ml/final_model"
FINAL_MODEL_FILE_NAME = "GradientBoostingClassifier.pkl"