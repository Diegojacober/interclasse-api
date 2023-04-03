from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import Path

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.jogos import JogoModel
from schemas.jogos_schema import JogoSchema
from core.deps import get_session


router = APIRouter()

#POST modalidade
@router.post("/", status_code=status.HTTP_201_CREATED, response_model= JogoSchema)
async def post_modalidade(jogo: JogoSchema, db: AsyncSession = Depends(get_session)):
    novo_jogo = JogoModel(time1=jogo.time1,
                                      time2=jogo.time2,
                                      data_jogo=jogo.data_do_jogo,)

    db.add(novo_jogo)
    await db.commit()

    return novo_jogo
