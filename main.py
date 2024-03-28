from source.entity.config_entity import TrainingPipelineConfig
import pandas as pd

if __name__ == '__main__':

    train_pipeline_config_obj = TrainingPipelineConfig()

    print(train_pipeline_config_obj.__dict__)