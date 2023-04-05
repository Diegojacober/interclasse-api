from typing import Optional

from pydantic import BaseModel as SCBaseModel

class AtletaSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    idade: int
    face_url: Optional[str]
    curso_id: int
    modalidade_id: int
    curso: str
    modalidade: str

    class Config:
        orm_mode = True