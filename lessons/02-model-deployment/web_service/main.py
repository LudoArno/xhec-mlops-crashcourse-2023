from fastapi import FastAPI
import lib.models as models
import app_config
from typing import List

# Initiate the FastAPI app
app = FastAPI()

# Initiate the homepage of the API
@app.get("/")
def index():
    return {"title": app_config.APP_TITLE,
            "Description": app_config.APP_DESCRIPTION,
            "Version": app_config.APP_VERSION,
            "Model Version": app_config.MODEL_VERSION,
            "Path to Pipeline": app_config.PATH_TO_PIPELINE,
            }

# Define a POST operation for the path "/predict"
@app.post("/predict")
def run_inference(item: List[models.Input_raw]):
    print(f"Received request: {item}")
    
    results = models.process_predict(item)
    return {"prediction results": results.tolist()}