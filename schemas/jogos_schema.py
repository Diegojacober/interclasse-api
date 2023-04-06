from typing import Optional

from pydantic import BaseModel as SCBaseModel

class JogoSchema(SCBaseModel):
    id: Optional[int]
    time1: int
    time2: int
    data_do_jogo: str
    time1_nome: Optional[str]
    time2_nome: Optional[str]
    
    class Config:
        orm_mode = True