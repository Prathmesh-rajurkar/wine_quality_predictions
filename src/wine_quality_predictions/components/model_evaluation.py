import pandas as pd
import numpy as np
import os 
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import joblib
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
from src.wine_quality_predictions import logger
from src.wine_quality_predictions.entity.config_entity import ModelEvaluationConfig
from src.wine_quality_predictions.constants import *
from src.wine_quality_predictions.utils.common import read_yaml,create_directories,save_json


os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/prathmeshrajurkar199/wine_quality_predictions.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'prathmeshrajurkar199'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'eb03a5acc285ba6cf90c217e1cc722a07eb7e34f'

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            print(predicted_qualities)
            (rmse,mae,r2) = self.eval_metrics(test_x,predicted_qualities)

            scores = {'rmse':rmse,'mae':mae,'r2':r2}
            save_json(path = Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)

            if tracking_uri_type_store != 'file':
                mlflow.sklearn.log_model(model,'model',registered_model_name='ElasticNetModel')
            else:
                mlflow.sklearn.log_model(model,'model')