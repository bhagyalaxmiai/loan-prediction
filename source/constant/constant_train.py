# common constants
import certifi
ca = certifi.where()

TARGET_COLUMN = 'Loan_Status'
TRAIN_PIPELINE_NAME = 'training_pipeline'
ARTIFACT_DIR = 'artifact'
FILE_NAME = 'training_data.csv'

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

MONGO_DB_URL_KEY = 'mongodb+srv://veenagabnave:aa5xcuda8yrgb6Zd@cluster0.otxvmcd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsCAFile=' + ca
DATABASE_NAME = 'loan-prediction'

# Data Ingestion Constants
DI_COLLECTION_NAME = 'loan-train-data'
DI_DIR_NAME = 'data_ingestion'
DI_FEATURE_STORE_DIR = 'feature_store'
DI_INGESTED_DIR = 'ingested'
DI_TRAIN_TEST_SPLIT_RATIO = 0.2

