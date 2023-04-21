from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

import os
import urllib

#DATABASE_URL = "sqlite:///./test.db"


class Settings(BaseSettings):
    """
     Configurações gerais para a aplicação
    """
    API_V1_STR: str = '/api/v1'
    
    #conexão local
    # DB_URL: str = "mysql+asyncmy://root:Di29122004#@localhost:3306/interclasse"
    # host_server = os.environ.get('host_server', 'localhost')
    # db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
    # database_name = os.environ.get('database_name', 'fastapi')
    # db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
    # db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'secret')))
    # ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
    # DB_URL = 'mysql+asyncmy://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
    DB_URL: str = "mysql+asyncmy://diegos@interclasse-2023:senaimange2023@interclasse-2023.mariadb.database.azure.com:3306/interclasse"
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
