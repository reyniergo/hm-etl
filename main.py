from etl_pokeapi import ETLPokeAPI

if __name__ == "__main__":
    """
    Configuración para la conexión a MySQL.
    """

    mysql_config = {
        "USER": "hm_testing",
        "PASSWORD": "rv1EknPdH5DYi2g",
        "HOST": "152.53.88.66",
        "PORT": 3306,
        "DATABASE": "DLX_HM_DB"
    }

    etl = ETLPokeAPI(mysql_config)
    etl.run()