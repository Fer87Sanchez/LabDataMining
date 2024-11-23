import joblib  # Importar joblib para cargar el modelo
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Crear la aplicación FastAPI
app = FastAPI()

# Cargar el modelo desde el archivo .joblib
model_path = "./random_forest_model.joblib"
model = joblib.load(model_path)

# Definir la estructura de los datos de entrada
class PredictionRequest(BaseModel):
    annual_income: float
    total_spent: float
    avg_purchase_value: float
    online_activity_score: float
    gender_male: int  # 1 si es hombre, 0 si es mujer

# Endpoint para verificar el estado de la API
@app.get("/")
def read_root():
    return {"message": "Modelo Random Forest API está funcionando correctamente"}

# Endpoint para realizar predicciones
@app.post("/predict")
def predict(request: PredictionRequest):
    # Convertir los datos de entrada en un array para el modelo
    input_data = np.array([[request.annual_income, 
                            request.total_spent, 
                            request.avg_purchase_value, 
                            request.online_activity_score, 
                            request.gender_male]])
    
    try:
        # Realizar la predicción
        prediction = model.predict(input_data)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error en la predicción: {e}")
