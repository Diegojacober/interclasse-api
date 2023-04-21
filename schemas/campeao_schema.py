from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CampeaoSchema(SCBaseModel):
    id: Optional[int]
    time: int
    modalidade_id: int
    time_nome: Optional[str]
    modalidade: Optional[str]
    
    class Config:
        orm_mode = True