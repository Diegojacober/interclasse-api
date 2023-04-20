from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
     Configurações gerais para a aplicação
    """
    API_V1_STR: str = '/api/v1'
    
    #conexão local
    # DB_URL: str = "mysql+asyncmy://root:Di29122004#@localhost:3306/interclasse"
    DB_URL: str = "mysql+asyncmy://diegos@interclasse-2023:senaimange2023@interclasse-2023.mariadb.database.azure.com:3306/interclasse"
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
