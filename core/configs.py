from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
     Configurações gerais para a aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+asyncmy://root:@localhost:3306/interclasse"
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
