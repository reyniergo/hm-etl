import requests
import pandas as pd
from sqlalchemy import create_engine
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler("etl.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Clase ETLPokeAPI
class ETLPokeAPI:
    def __init__(self, mysql_config, limit=50):
        self.mysql_config = mysql_config
        self.limit = limit

    def extraer(self):
        """Extrae la lista de Pokémon desde la PokeAPI."""
        try:
            url = f"https://pokeapi.co/api/v2/pokemon?limit={self.limit}"
            logger.info(f"Solicitando datos desde: {url}")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            pokemon_list = []
            for pokemon in data['results']:
                detail_response = requests.get(pokemon['url'])
                detail_response.raise_for_status()
                details = detail_response.json()
                pokemon_list.append(details)

            logger.info(f"{len(pokemon_list)} Pokémon extraídos exitosamente.")
            return pokemon_list

        except requests.RequestException as e:
            logger.error(f"❌ Error al extraer datos de la API: {e}")
            return []

    def transformar(self, pokemon_list):
        """Transforma la lista de Pokémon en un DataFrame con los campos."""
        if not pokemon_list:
            logger.warning("⚠️ Lista de Pokémon vacía. No se puede transformar.")
            return pd.DataFrame()

        try:
            transformed = []
            for pokemon in pokemon_list:
                types = [t['type']['name'] for t in pokemon['types']]
                transformed.append({
                    'id': pokemon['id'],
                    'name': pokemon['name'],
                    'height': pokemon['height'],
                    'weight': pokemon['weight'],
                    'types': ', '.join(types)
                })

            df = pd.DataFrame(transformed)
            logger.info("Datos transformados correctamente.")
            return df
        except Exception as e:
            logger.error(f"❌ Error durante la transformación: {e}")
            return pd.DataFrame()

    def cargarDb(self, df):
        """Carga el DataFrame en la tabla 'POKEMON' de MySQL."""
        if df.empty:
            logger.warning("⚠️ DataFrame vacío. No se cargará en la base de datos.")
            return

        try:
            user = self.mysql_config.get('USER')
            password = self.mysql_config.get('PASSWORD')
            host = self.mysql_config.get('HOST', 'localhost')
            port = self.mysql_config.get('PORT', 3306)
            database = self.mysql_config.get('DATABASE')

            engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
            df.to_sql('POKEMON', con=engine, if_exists='replace', index=False)
            logger.info("✅ Datos cargados en MySQL correctamente.")
        except Exception as e:
            logger.error(f"❌ Error al cargar datos en MySQL: {e}")

    def run(self):
        """Ejecuta el proceso ETL: extraer, transformar y cargar."""
        logger.info("🚀 Iniciando proceso ETL de PokeAPI...")
        data = self.extraer()
        df = self.transformar(data)
        self.cargarDb(df)
        logger.info("✅ Proceso ETL finalizado.")