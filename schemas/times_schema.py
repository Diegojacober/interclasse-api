from typing import Optional

from pydantic import BaseModel as SCBaseModel

class TimeSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    pontos: int
    jogador1: int
    jogador2: Optional[int]
    jogador3: Optional[int]
    jogador4: Optional[int]
    jogador5: Optional[int]
    jogador6: Optional[int]
    jogador7: Optional[int]
    jogador8: Optional[int]
    jogador9: Optional[int]
    jogador10: Optional[int]
    
    jogador1_nome: Optional[str]
    jogador2_nome: Optional[str]
    jogador3_nome: Optional[str]
    jogador4_nome: Optional[str]
    jogador5_nome: Optional[str]
    jogador6_nome: Optional[str]
    jogador7_nome: Optional[str]
    jogador8_nome: Optional[str]
    jogador9_nome: Optional[str]
    jogador10_nome: Optional[str]
    

    class Config:
        orm_mode = True