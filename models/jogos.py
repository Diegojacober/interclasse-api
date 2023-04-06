from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from models.times import TimeModel


class JogoModel(settings.DB_BASE_MODEL):
    __tablename__ = "jogos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    time1: int = Column(Integer, ForeignKey("times.id", ondelete="CASCADE"), nullable=False)
    time2: int = Column(Integer, ForeignKey("times.id", ondelete="CASCADE"), nullable=False)
    data_do_jogo = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


