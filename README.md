# Usage of microservice
    ```
    cd microservice/
    uvicorn app:app --reload
    http POST http://127.0.0.1:8000/predict_knn features:='[45, 260000, 0, 0.6, 0.7, 3, -6, 0.1, 0.2, 0.0, 0.3, 0.8, 120, 4]'
    http POST http://127.0.0.1:8000/predict_sgd features:='[45, 260000, 0, 0.6, 0.7, 3, -6, 0.1, 0.2, 0.0, 0.3, 0.8, 120, 4]'
    ```