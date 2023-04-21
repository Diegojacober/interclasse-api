from typing import Optional

from pydantic import BaseModel as SCBaseModel

class AtletaSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    idade: int
    face_url: Optional[str]
    curso_id: int
    modalidade_id: int
    curso: Optional[str]
    modalidade: Optional[str]
    proximos_jogos: Optional[list]
    
    class Config:
        orm_mode = True