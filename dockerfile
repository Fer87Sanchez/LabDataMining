# Usa la imagen base oficial de Python
FROM python:3.9-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
COPY app.py .
COPY random_forest_model.joblib .
COPY startup.sh .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Asegúrate de que el script tenga permisos de ejecución
RUN chmod +x /app/startup.sh

# Expone el puerto 8000 para FastAPI
EXPOSE 8000

# Usa el script startup.sh como comando de inicio
CMD ["/app/startup.sh"]

