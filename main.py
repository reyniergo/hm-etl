from etl_pokeapi import ETLPokeAPI

if __name__ == "__main__":
    """
    Configuración para la conexión a MySQL.
    """

    mysql_config = {
        "USER": "root",
        "PASSWORD": "Raynier1205*",
        "HOST": "152.53.53.245",
        "PORT": 3306,
        "DATABASE": "DLX_HM_DB"
    }

    etl = ETLPokeAPI(mysql_config)
    etl.run()