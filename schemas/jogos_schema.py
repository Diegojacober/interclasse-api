from typing import Optional

from pydantic import BaseModel as SCBaseModel

class AtletaSchema(SCBaseModel):
    id: Optional[int]
    time1: int
    time2: int
    data_do_jogo: str

    class Config:
        orm_mode = True