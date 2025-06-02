from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        train_pipeline_config = TrainingPipelineConfig()
        data_ingest_config = DataIngestionConfig(train_pipeline_config)
        data_ingest= DataIngestion(data_ingest_config)
        data_ingest_artifact=data_ingest.initiate_data()
        print(data_ingest_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)