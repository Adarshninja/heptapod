from fastapi import FastAPI
import numpy as np
from sklearn.ensemble import IsolationForest

app = FastAPI()

#Train a simple model on dummy data
np.random.seed(42)
train_data = np.random.normal(0, 1, (100, 3))


model = IsolationForest(contamination=0.1)
model.fit(train_data)

@app.get("/")
def home():
    return {"message": "ML4DQM Anomaly Detection API is running"}



@app.post("/predict")
def predict(data: list):
    data = np.array(data).reshape(1, -1)


    score= model.decision_function(data)[0]
    prediction = model.predict(data)[0]

    return {
        "anomaly_score": float(score),
        "is_anomaly": True if prediction == -1 else False
    }
    