from src.wine_quality_predictions import logger
from src.wine_quality_predictions.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_quality_predictions.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


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