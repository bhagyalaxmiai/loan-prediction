import os
from source.constant import constant_train


class TrainingPipelineConfig:
    def __init__(self, global_timestamp):
        self.artifact_dir = os.path.join(constant_train.ARTIFACT_DIR, global_timestamp)
        self.global_timestamp = global_timestamp
        self.target_column = constant_train.TARGET_COLUMN
        self.train_pipeline = constant_train.TRAIN_PIPELINE_NAME

        # Data Ingestion constant
        self.di_dir = os.path.join(self.artifact_dir, constant_train.DI_DIR_NAME)
        self.feature_store_dir_path = os.path.join(self.di_dir, constant_train.DI_FEATURE_STORE_DIR, constant_train.FILE_NAME)
        self.train_file_path = os.path.join(self.di_dir, constant_train.DI_INGESTED_DIR, constant_train.TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.di_dir, constant_train.DI_INGESTED_DIR, constant_train.TEST_FILE_NAME)
        self.train_test_split_ratio = constant_train.DI_TRAIN_TEST_SPLIT_RATIO
        self.mongodb_url_key = os.environ['MONGODB_KEY']
        self.database_name = constant_train.DATABASE_NAME
        self.collection_name = constant_train.DI_COLLECTION_NAME
        self.mandatory_column_list = constant_train.DI_MANDATORY_COLUMN_LIST
        self.mandatory_column_datatype = constant_train.DI_MANDATORY_COLUMN_DATA_TYPE

        # DATA VALIDATION
        self.imputation_values_file = constant_train.DV_IMPUTATION_VALUES_FILE
        self.outliers_params_file = constant_train.DV_OUTLIERS_PARAMS_FILE
        self.dv_train_file_path = os.path.join(self.artifact_dir,constant_train.DV_DIR_NAME)
        self.dv_test_file_path = os.path.join(self.artifact_dir, constant_train.DV_DIR_NAME)
        self.train_file_name = constant_train.TRAIN_FILE_NAME
        self.test_file_name = constant_train.TEST_FILE_NAME

        # data transformation
        self.dt_binary_class_col = constant_train.DT_BINARY_CLASS_COL
        self.dt_multi_class_col = constant_train.DT_MULTI_CLASS_COL
        self.dt_multi_class_encoder = constant_train.DT_ENCODER_PATH
        self.dt_multi_class_encoder = constant_train.DT_ENCODER_PATH
        self.dt_train_file_path = os.path.join(self.artifact_dir, constant_train.DT_DIR_NAME)
        self.dt_test_file_path = os.path.join(self.artifact_dir, constant_train.DT_DIR_NAME)

        # Model Train And Evaluate
        self.model_path = os.path.join(constant_train.MODEL_PATH)
        self.final_model_path = os.path.join(constant_train.FINAL_MODEL_PATH)
        self.final_model_name = constant_train.FINAL_MODEL_FILE_NAME
