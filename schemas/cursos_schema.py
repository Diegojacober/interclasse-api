from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id: Optional[int]
    curso: str

    class Config:
        orm_mode = True