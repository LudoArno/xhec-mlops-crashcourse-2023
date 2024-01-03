# hello_world.py
from prefect import flow, serve
from workflows import train_model_workflow, batch_predict_workflow

from config import *


if __name__ == "__main__":
    train_deployment = train_model_workflow.to_deployment(
        name='Hello world Deployment',
        version='0.1.0',
        tags=['hello world'],
        interval=600,
        parameters={
            "train_filepath": train_path,
            "test_filepath": test_path
        })
    predict_deployment = batch_predict_workflow.to_deployment(
        name='my batch predict deployment',
        version='0.1.0',
        tags=["predict", "taxi"],
        interval=600,
        parameters={
            "input_filepath": predict_path,
            "model": train_deployment["model"],
            "dv": train_deployment["dv"]
        }
    )
    
    # Above: can be tested in notebook. Below: must be called from python script
    # serve(train_deployment) 
    #this will not work because the flow are not supposed to return any value, 
    # we should have saved and loaded model, dv and evaluation in pickle