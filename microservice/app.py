from fastapi import FastAPI, HTTPException, File,  UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import joblib
import numpy as np
import random
import csv
from datetime import datetime
import jsonlines
import logging
from typing import List

app = FastAPI()

# Load models and scalers for different variations
model_variations = {
    "sgd": {
        "model": joblib.load("../models/scikit_sgd_model.joblib"),
        "scaler": joblib.load("../models/scikit_sgd_scaler.joblib"),
    },
    "knn_randomsearch": {
        "model": joblib.load("../models/scikit_knn_model_with_hyperparameters.joblib"),
        "scaler": joblib.load("../models/scikit_knn_scaler_with_hyperparameters.joblib"),
    },
}

class Item(BaseModel):
    features: list

def setup_logging():
    try:
        logging.basicConfig(filename="model_logs.log", level=logging.INFO,
                            format='%(asctime)s [%(levelname)s] %(message)s')
    except Exception as e:
        print(f"Error setting up logging: {e}")

def log_model_call(variation, input_data, processed_data, prediction, error=None):
    log_msg = f"Model Variation: {variation}\nInput Data: {input_data}\nProcessed Data: {processed_data}\nPrediction: {prediction}\nError: {error}\n"
    logging.info(log_msg)

def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

@app.post("/predict/{variation}")
def predict(item: Item, variation: str):
    try:
        if variation not in model_variations:
            raise HTTPException(status_code=400, detail="Invalid model variation")

        model_info = model_variations[variation]
        input_data = item.features
        processed_data = model_info["scaler"].transform(np.array(input_data).reshape(1, -1))
        prediction = model_info["model"].predict(processed_data)
        log_model_call(variation, input_data, processed_data.tolist(), prediction.tolist())

        # Log model call to CSV
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = [timestamp, variation, str(prediction[0])]
        write_to_csv("model_logs.csv", log_data)

        return {"predicted_genre": str(prediction[0])}
    except Exception as e:
        # Log model call with error
        log_model_call(variation, input_data, processed_data.tolist(), prediction.tolist(), error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

def ab_test_single_record(record, variation):
    try:
        model_info = model_variations[variation]
        input_data = record["features"]
        processed_data = model_info["scaler"].transform(np.array(input_data).reshape(1, -1))
        prediction = model_info["model"].predict(processed_data)

        # Log model call
        log_model_call(variation, input_data, processed_data.tolist(), prediction.tolist())

        # Log model call to CSV
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = [timestamp, variation, str(prediction[0])]
        write_to_csv("model_logs.csv", log_data)

        return {"predicted_genre": str(prediction[0])}
    except Exception as e:
        # Log model call with error
        log_model_call(variation, input_data, processed_data.tolist(), prediction.tolist(), error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ab_test")
async def ab_test(file: UploadFile = File(...)):
    # file_content = await file.read()
    # try:
    #     with jsonlines.open(file, 'r') as reader:
    #         for record in reader:
    #             # Randomly choose a model variation for A/B testing
    #             variation = random.choice(list(model_variations.keys()))

    #             # Perform A/B test for a single record
    #             ab_test_single_record(record, variation)
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))


    # try:
    #     # Process each uploaded file
    #     for file in files:
    #         contents = await file.read()
            
    #         # Do something with the contents, e.g., save it to disk or process it
    #         # In this example, we are printing the filename and size
    #         print(f"Uploaded file: {file.filename}, Size: {len(contents)} bytes")
    #     return JSONResponse(content={"message": "File(s) uploaded successfully"})
    # except Exception as e:
    #     return JSONResponse(content={"detail": str(e)}, status_code=500)
    content = await file.read()
    
    # Process the content as needed
    # In this example, we just print the content
    print(content.decode())
    
    return {"message": "File uploaded successfully"}

if __name__ == "__main__":
    setup_logging()
