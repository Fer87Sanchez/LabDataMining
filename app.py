from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np
import pandas as pd

# Cargar el modelo entrenado
model_path = './randomforestmodel.joblib'
model = load(model_path)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Clase para el cuerpo de la solicitud
class CustomerData(BaseModel):
    annual_income: float
    total_spent: float
    avg_purchase_value: float
    online_activity_score: float
    gender_male: int  # Género codificado como 0 o 1

# Ruta de prueba
@app.get("/")
def home():
    return {"message": "Modelo de clasificación activo"}

# Ruta para predicciones
@app.post("/predict")
def predict(data: CustomerData):
    # Convertir los datos en un array numpy
    input_data = np.array([[
        data.annual_income,
        data.total_spent,
        data.avg_purchase_value,
        data.online_activity_score,
        data.gender_male
    ]])
    # Realizar la predicción
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}

