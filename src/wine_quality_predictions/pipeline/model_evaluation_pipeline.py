from src.wine_quality_predictions.entity.config_entity import ModelEvaluationConfig
from src.wine_quality_predictions.config.configuration import ConfigurationManager
from src.wine_quality_predictions.components.model_evaluation import ModelEvaluation
from src.wine_quality_predictions import logger
from pathlib import Path

STAGE_NAME = 'Model Evaluation Stage'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
        model_trainer = ModelEvaluationTrainingPipeline()
        model_trainer.initiate_model_evaluation()
        logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error
