from core.configs import settings
from sqlalchemy import Column, Integer, String


class ModalidadeModel(settings.DB_BASE_MODEL):
    __tablename__ = "modalidades"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(50), nullable=False)
    team: str = Column(String(1), nullable=False)
    duo: str = Column(String(1), nullable=False)
    individual: str = Column(String(1), nullable=False)

