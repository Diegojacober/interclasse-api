
from core.configs import settings
from sqlalchemy import Column, Integer, String

class CursoModel(settings.DB_BASE_MODEL):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    curso: str = Column(String(100), nullable=False)

