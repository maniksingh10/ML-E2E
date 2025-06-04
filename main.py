from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig,TrainingPipelineConfig, DataTransformationConfig, ModelTrainerConfig

import sys

if __name__ == '__main__':
    try:
        train_pipeline_config = TrainingPipelineConfig()
       
        data_ingest_config = DataIngestionConfig(train_pipeline_config)
        data_ingest= DataIngestion(data_ingest_config)
        data_ingest_artifact=data_ingest.initiate_data()
        
        data_validation_config = DataValidationConfig(train_pipeline_config)
        data_validate = DataValidation(data_ingest_artifact,data_validation_config)
        data_validate_artifact=data_validate.initiate_data_validation()

        data_transform_config = DataTransformationConfig(train_pipeline_config)
        data_transform =DataTransformation(data_validate_artifact, data_transform_config)
        data_transform_artifact = data_transform.initiate_data_transformation()

        model_trainer_config=ModelTrainerConfig(train_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transform_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
