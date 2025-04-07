# Imagen base oficial de Python
FROM python:3.11-slim

# Variables de entorno para evitar que Python cree archivos .pyc y use buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Actualiza e instala dependencias del sistema necesarias para pymysql y requests
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando por defecto al correr el contenedor
CMD ["python", "main.py"]
