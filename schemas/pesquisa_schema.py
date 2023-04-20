from typing import Optional

from pydantic import BaseModel as SCBaseModel

class ImageSearchSchema(SCBaseModel):
    id: Optional[int]
    nome_imagem: str
    horario: str
    
    class Config:
        orm_mode = True