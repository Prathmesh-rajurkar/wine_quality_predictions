from src.wine_quality_predictions.entity.config_entity import DataValidationConfig
from src.wine_quality_predictions.config.configuration import ConfigurationManager
from src.wine_quality_predictions.components.data_validation import DataValidation
from src.wine_quality_predictions import logger

STAGE_NAME = 'Data Validatation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error