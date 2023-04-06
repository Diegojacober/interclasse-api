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
from models.times import TimeModel
from schemas.jogos_schema import JogoSchema
from core.deps import get_session


router = APIRouter()

#POST jogo
@router.post("/", status_code=status.HTTP_201_CREATED, response_model= JogoSchema)
async def post_jogo(jogo: JogoSchema, db: AsyncSession = Depends(get_session)):
    novo_jogo = JogoModel(time1=jogo.time1,
                                      time2=jogo.time2,
                                      data_do_jogo=jogo.data_do_jogo,)

    db.add(novo_jogo)
    await db.commit()

    return novo_jogo

#get jogos
@router.get('/', response_model=List[JogoSchema])
async def get_atletas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(JogoModel)
        result = await session.execute(query)
        jogos: List[JogoModel] = result.scalars().all()
        
        query = select(TimeModel)
        result = await session.execute(query)
        times: List[TimeModel] = result.scalars().all()
        
        for jogo in jogos:
            jogo.data_do_jogo = str(jogo.data_do_jogo)
            for time in times:
                if time.id == jogo.time1:
                   jogo.time1_nome = time.nome
                
                if time.id == jogo.time2:
                   jogo.time2_nome = time.nome
                   
           
        return jogos
