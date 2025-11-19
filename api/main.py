from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# Load model (using full path)
MODEL_PATH = r"C:\Users\Ashwini\Documents\medilink\models\model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Input format for prediction
class PatientData(BaseModel):
    age: float
    blood_pressure: float
    heart_rate: float
    symptoms_score: float

@app.post("/predict")
def predict(data: PatientData):
    # Convert input into numpy array
    X = np.array([[data.age, data.blood_pressure, data.heart_rate, data.symptoms_score]])

    # Make prediction
    prediction = model.predict(X)[0]

    # Return result
    return {"prediction": int(prediction)}



