from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.atletas import AtletaModel


class TimeModel(settings.DB_BASE_MODEL):
    __tablename__ = "times"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(150), nullable=False)
    pontos: int = Column(Integer, nullable=False)
    jogador1: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador2: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador3: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador4: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador5: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador6: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador7: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador8: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador9: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)
    jogador10: int = Column(Integer, ForeignKey(AtletaModel.id), primary_key=True)

    jogador_1 = relationship('atletas', foreign_keys='times.jogador1')
    jogador_2 = relationship('atletas', foreign_keys='times.jogador2')
    jogador_3 = relationship('atletas', foreign_keys='times.jogador3')
    jogador_4 = relationship('atletas', foreign_keys='times.jogador4')
    jogador_5 = relationship('atletas', foreign_keys='times.jogador5')
    jogador_6 = relationship('atletas', foreign_keys='times.jogador6')
    jogador_7 = relationship('atletas', foreign_keys='times.jogador7')
    jogador_8 = relationship('atletas', foreign_keys='times.jogador8')
    jogador_9 = relationship('atletas', foreign_keys='times.jogador9')
    jogador_10 = relationship('atletas', foreign_keys='times.jogador10')
