from core.configs import settings
from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from models.cursos import CursoModel
from models.modalidades import ModalidadeModel


class ImageSearchModel(settings.DB_BASE_MODEL):
    __tablename__ = "pesquisasimagens"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome_imagem: str = Column(String(255), nullable=False)
    horario = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))