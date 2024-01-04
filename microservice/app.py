from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../models/scikit_knn_model.joblib")
scaler = joblib.load("../models/scikit_knn_scaler.joblib")

class Item(BaseModel):
    features: List[float]

@app.post("/predict")
def predict(item: Item):
    try:
        new_song = np.array(item.features).reshape(1, -1)
        new_song = scaler.transform(new_song)
        predicted_genre = model.predict(new_song)
        
        return {"predicted_genre": str(predicted_genre[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
