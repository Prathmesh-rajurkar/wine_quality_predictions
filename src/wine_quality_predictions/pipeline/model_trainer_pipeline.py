from src.wine_quality_predictions.entity.config_entity import ModelTrainerConfig
from src.wine_quality_predictions.config.configuration import ConfigurationManager
from src.wine_quality_predictions.components.model_trainer import ModelTrainer
from src.wine_quality_predictions import logger
from pathlib import Path

STAGE_NAME='Model Training Stage'

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as error:
            raise error

if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.initiate_model_trainer()
        logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error
