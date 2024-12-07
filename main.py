from src.wine_quality_predictions import logger
from src.wine_quality_predictions.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_quality_predictions.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.wine_quality_predictions.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.wine_quality_predictions.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline

logger.info("Welcome to our custom logging library")



STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> Stage : {STAGE_NAME} ended <<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error



STAGE_NAME = 'Data Validatation Stage'
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error




STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error



STAGE_NAME = 'Model Training Stage'
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error