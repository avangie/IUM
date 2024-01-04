from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np

app = FastAPI()

model_knn = joblib.load("../models/scikit_knn_model.joblib")
scaler_knn = joblib.load("../models/scikit_knn_scaler.joblib")
model_sgd = joblib.load("../models/scikit_sgd_model.joblib")
scaler_sgd = joblib.load("../models/scikit_sgd_scaler.joblib")

class Item(BaseModel):
    features: List[float]

@app.post("/predict_knn")
def predict(item: Item):
    try:
        new_song = np.array(item.features).reshape(1, -1)
        new_song = scaler_knn.transform(new_song)
        predicted_genre = model_knn.predict(new_song)
        
        return {"predicted_genre": str(predicted_genre[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_sgd")
def predict_sgd(item: Item):
    try:
        new_song = np.array(item.features).reshape(1, -1)
        new_song = scaler_sgd.transform(new_song)
        predicted_genre = model_sgd.predict(new_song)
        
        return {"predicted_genre": str(predicted_genre[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))