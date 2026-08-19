iris Flower Classification API
A machine learning API that predicts the species of an Iris flower based on its sepal and petal measurements.
The project uses Logistic Regression and exposes the trained model through a FastAPI REST API. The API is deployed on Render.
Project Overview
The model predicts one of three Iris flower species:
Setosa
Versicolor
Virginica
Input Features
The API accepts four features:
Sepal Length
Sepal Width
Petal Length
Petal Width
Machine Learning Model
Model: Logistic Regression
The preprocessing and classification model are combined using a Scikit-learn Pipeline.
Model Accuracy
The Logistic Regression model achieved:
Accuracy: 1.0 (100%)
on the test set.
Technologies Used
Python
Scikit-learn
Pandas
FastAPI
Pydantic
Uvicorn
Joblib
GitHub
Render
Project Structure
iris-fastapi-api/
│
├── main.py
├── iris_model.pkl
├── requirements.txt
└── README.md
