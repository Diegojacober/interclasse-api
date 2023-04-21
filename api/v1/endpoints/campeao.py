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
from models.campeao import CampeaoModel
from models.modalidades import ModalidadeModel
from schemas.jogos_schema import JogoSchema
from schemas.modalidades_schema import ModalidadeSchema
from schemas.campeao_schema import CampeaoSchema
from core.deps import get_session
import datetime


router = APIRouter()


@router.get('/campeao', response_model=List[CampeaoSchema], status_code=status.HTTP_200_OK)
async def get_campeoes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CampeaoModel)
        result = await session.execute(query)
        campeoes: List[CampeaoModel] = result.scalars().all()
        
        query = select(TimeModel)
        result = await session.execute(query)
        times: List[TimeModel] = result.scalars().all()
        
        
        query = select(ModalidadeModel)
        result = await session.execute(query)
        modalidades: List[ModalidadeModel] = result.scalars().fetchall()
        
        for campeao in campeoes:
            
            for modalidade in modalidades:
                if campeao.modalidade_id == modalidade.id:
                    campeao.modalidade = modalidade.nome
            
            for time in times:
                if campeao.time == time.id:
                    campeao.time_nome = time.nome
                  
        return campeoes
    



@router.post("/", status_code=status.HTTP_201_CREATED, response_model= CampeaoSchema)
async def post_campeao(campeao: CampeaoSchema, db: AsyncSession = Depends(get_session)):
    novo_campeao = CampeaoModel(modalidade_id=campeao.modalidade_id, time=campeao.time)

    db.add(novo_campeao)
    await db.commit()

    return novo_campeao
