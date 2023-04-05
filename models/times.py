from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship
from models.atletas import AtletaModel


class TimeModel(settings.DB_BASE_MODEL):
    __tablename__ = "times"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(150), nullable=False)
    pontos: int = Column(Integer, nullable=False)
    jogador1: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"))
    jogador2: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador3: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador4: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador5: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador6: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador7: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador8: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador9: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))
    jogador10: int = Column(Integer, ForeignKey("atletas.id", ondelete="CASCADE"), default=text("Null"))

