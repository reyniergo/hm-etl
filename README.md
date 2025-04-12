# HM ETL ![HM ETL](https://img.shields.io/badge/version-1.0.0-blue.svg)

## Descripción 📜

Este proyecto implementa un proceso **ETL** (Extracción, Transformación y Carga) que extrae datos de la **PokeAPI**, los transforma en un formato adecuado y luego los carga en una base de datos **MySQL**. El objetivo es gestionar los datos de los Pokémon de forma eficiente utilizando Python, SQLAlchemy y pymysql.

## Requisitos 📋

Este proyecto necesita algunas dependencias para funcionar correctamente:

- **Python 3.11** o superior ![Python](https://img.shields.io/badge/python-3.11-blue.svg)
- **MySQL** como base de datos ![MySQL](https://img.shields.io/badge/MySQL-8.0-blue.svg)
- **Dependencias de Python**:
  - pandas 📊
  - requests 🌐
  - SQLAlchemy 🔗
  - pymysql 🐬
  - logging 📜 (para manejo de logs)


## Instalación 🛠️

1. Clona el repositorio:

   ```bash
   git clone https://github.com/ReynierGo/hm-etl.git
   cd hm-etl

2. Para ejecutar el contenedor docker

   ```bash
   docker build -t hm-etl .
   docker run --rm hm-etl
