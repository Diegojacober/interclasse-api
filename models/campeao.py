
from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey

class CampeaoModel(settings.DB_BASE_MODEL):
    __tablename__ = "campeoes"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    modalidade_id: int = Column(Integer, ForeignKey("modalidades.id", ondelete="CASCADE"), nullable=False)
    time: int = Column(Integer, ForeignKey("times.id", ondelete="CASCADE"), nullable=False)

