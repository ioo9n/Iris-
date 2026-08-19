from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Iris Prediction API is running"}

@app.post("/predict")
def predict(iris: IrisInput):
    feature = [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
    prediction = model.predict(feature)
    pred_val = int(prediction[0])
    classes = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    return {
        "prediction": pred_val,
        "class": classes[pred_val]
    }
