from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Cargar el modelo y el codificador de etiquetas
model = joblib.load("random_forest_model.joblib")
label_encoder = joblib.load("label_encoder.joblib")

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir la entrada esperada 
class CustomerData(BaseModel):
    age: int
    gender: str
    annual_income: float
    total_spent: float
    avg_purchase_value: float
    online_activity_score: float
    loyalty_program: int
    days_since_last_purchase: int
    num_site_visits: int

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"message": "La API está funcionando correctamente"}

# Endpoint para realizar predicciones
@app.post("/predict/")
def predict(data: CustomerData):
    # Convertir la entrada en un DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Procesar columnas categóricas como 'gender'
    input_data = pd.get_dummies(input_data, columns=["gender"], drop_first=True)
    
    
    missing_cols = set(model.feature_names_in_) - set(input_data.columns)
    for col in missing_cols:
        input_data[col] = 0
    input_data = input_data[model.feature_names_in_]

    # Hacer predicción
    prediction = model.predict(input_data)
    
    # Decodificar el resultado
    predicted_class = label_encoder.inverse_transform(prediction)[0]

    return {"predicted_class": predicted_class}
