from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.cursos import CursoModel
from models.modalidades import ModalidadeModel


class AtletaModel(settings.DB_BASE_MODEL):
    __tablename__ = "atletas"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(150), nullable=False)
    idade: int = Column(Integer, nullable=False)
    face_url: str = Column(String(255), nullable=True)
    curso_id: int = Column(Integer, ForeignKey(CursoModel.id), primary_key=True)
    modalidade_id: int = Column(Integer, ForeignKey(ModalidadeModel.id), primary_key=True)

    curso = relationship('cursos', foreign_keys='atletas.curso_id')
    modalidade = relationship('modalidade', foreign_keys='atletas.modalidade_id')

