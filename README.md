# Iris Flower Classification API

A machine learning API that predicts the species of an Iris flower based on its sepal and petal measurements.

The project uses **Logistic Regression** and exposes the trained model through a **FastAPI** REST API. The API is deployed on **Render**.

## Project Overview

The model predicts one of three Iris flower species:

* Setosa
* Versicolor
* Virginica

### Input Features

The API accepts four features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

## Machine Learning Model

**Model:** Logistic Regression

**Preprocessing:** StandardScaler

The preprocessing and classification model are combined using a Scikit-learn Pipeline.

### Model Accuracy

The Logistic Regression model achieved:

**Accuracy: 1.0 (100%)**

on the test set.

## Technologies Used

* Python
* Scikit-learn
* Pandas
* FastAPI
* Pydantic
* Uvicorn
* Joblib
* GitHub
* Render

## Project Structure

```text
iris-fastapi-api/
│
├── main.py
├── iris_model.pkl
├── requirements.txt
└── README.md
```

## API Endpoints

### GET `/`

Checks whether the API is running.

Example response:

```json
{
  "message": "Iris Prediction API is running"
}
```

### POST `/predict`

Predicts the Iris flower species.

#### Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

#### Response

```json
{
  "prediction": 0,
  "class": "Setosa"
}
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/iris-fastapi-api.git
cd iris-fastapi-api
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Deployment

The API is deployed using **Render**.

The deployment uses:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Live API

**API URL:** Add your Render URL here

**Swagger Documentation:** Add your Render `/docs` URL here

## Author

**Noor Alain Khaled Almatari**

Artificial Intelligence Student
Cairo University

