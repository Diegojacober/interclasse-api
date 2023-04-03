from typing import Optional

from pydantic import BaseModel as SCBaseModel

class AtletaSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    pontos: int
    jogador1: int
    jogador2: int
    jogador3: int
    jogador4: int
    jogador5: int
    jogador6: int
    jogador7: int
    jogador8: int
    jogador9: int
    jogador10: int

    class Config:
        orm_mode = True