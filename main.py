from src.wine_quality_predictions import logger
from src.wine_quality_predictions.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

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