from database.manage_db import manageDB
from fastapi import APIRouter
from ml.inference_classifier import InferenceClassifier
from models.models import MLRequest, MLResponse

inference_classifier = InferenceClassifier()
manage_db = manageDB(name_table="predictions")

routes_inference = APIRouter()


@routes_inference.post("/", response_model=MLResponse)
def inference_predict(request: MLRequest):
    prediction_list = inference_classifier.predict(input_data=request.input_data)
    ml_respose = MLResponse(prediction=prediction_list)
    manage_db.create(ml_respose.dict())
    return ml_respose


@routes_inference.get("/{id}", response_model=MLResponse)
def inference_predict_by_id(id: str):
    return manage_db.get(id)
