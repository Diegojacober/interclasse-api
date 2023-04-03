from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, DateTime
from sqlalchemy.orm import relationship
from models.times import TimeModel


class JogoModel(settings.DB_BASE_MODEL):
    __tablename__ = "jogos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    time1: int = Column(Integer, ForeignKey(TimeModel.id), primary_key=True)
    time2: int = Column(Integer, ForeignKey(TimeModel.id), primary_key=True)
    data_do_jogo = Column(DateTime(timezone=True))

    time_1 = relationship('times', foreign_keys='jogos.time1')
    time_2 = relationship('times', foreign_keys='jogos.time2')

