#!/bin/bash

# Verifica que el modelo esté presente
if [ ! -f "/app/random_forest_model.joblib" ]; then
    echo "Error: El archivo del modelo random_forest_model.joblib no se encuentra en /app."
    exit 1
fi

# Instala dependencias, en caso de ser necesario (por si el entorno no está completo)
pip install --no-cache-dir -r /app/requirements.txt

# Arranca la aplicación con Uvicorn
exec uvicorn app:app --host 0.0.0.0 --port 8000

