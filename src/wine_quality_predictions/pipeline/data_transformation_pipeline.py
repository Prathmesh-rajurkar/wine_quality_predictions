from src.wine_quality_predictions.entity.config_entity import DataTransformationConfig
from src.wine_quality_predictions.config.configuration import ConfigurationManager
from src.wine_quality_predictions.components.data_transformation import DataTransformation
from src.wine_quality_predictions import logger
from pathlib import Path

STAGE_NAME = 'Data Transformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as f:
                status = f.read().split(" ")[-1]
                print(status)
            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your Data Scheme is not valid")
        except Exception as error:
            print(error)


if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error