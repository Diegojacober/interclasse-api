from typing import Optional

from pydantic import BaseModel as SCBaseModel

class ModalidadeSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    team: str
    duo: str
    individual: str

    class Config:
        orm_mode = True