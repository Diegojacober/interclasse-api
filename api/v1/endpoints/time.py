from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import Path

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.atletas import AtletaModel
from models.times import TimeModel
from models.modalidades import ModalidadeModel
from schemas.times_schema import TimeSchema
from core.deps import get_session


router = APIRouter()


#POST time
@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_time(time: TimeSchema, db: AsyncSession = Depends(get_session)):
    
    
    if time.jogador2 == 0:
        time.jogador2 = None
        
    if time.jogador3 == 0:
        time.jogador3 = None
    
    if time.jogador4 == 0:
        time.jogador4 = None
        
    if time.jogador5 == 0:
        time.jogador5 = None    
    
    if time.jogador6 == 0:
        time.jogador6 = None
    
    if time.jogador7 == 0:
        time.jogador7 = None
        
    if time.jogador8 == 0:
        time.jogador8 = None
        
    if time.jogador9 == 0:
        time.jogador9 = None  
        
    if time.jogador10 == 0:
        time.jogador10 = None
    
    novo_time = TimeModel(nome=time.nome,
                              pontos=time.pontos,
                              jogador1=time.jogador1,
                              jogador2=time.jogador2,
                              jogador3=time.jogador3,
                              jogador4=time.jogador4,
                              jogador5=time.jogador5,
                              jogador6=time.jogador6,
                              jogador7=time.jogador7,
                              jogador8=time.jogador8,
                              jogador9=time.jogador9,
                              jogador10=time.jogador10,
                              modalidade_id=time.modalidade_id
                             )
    
    db.add(novo_time)
    await db.commit()
    return "Adicionado"


@router.get('/modalidade/{modalidade_id}', response_model=List[TimeSchema])
async def get_times_per_modalidade(modalidade_id: int = Path(title="ID da modalidade dos times desejados", description="Deve ser maior que 0", gt=0),db: AsyncSession = Depends(get_session)):
    
    async with db as session:
        query = select(TimeModel).where(TimeModel.modalidade_id == modalidade_id)
        result = await session.execute(query)
        times: TimeModel = result.scalars().all()

        if times:
            return times
        else:
            raise HTTPException(detail="Id não encontrado", status_code=status.HTTP_404_NOT_FOUND)

#GET times
@router.get('/', response_model=List[TimeSchema])
async def get_times(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TimeModel)
        result = await session.execute(query)
        times: List[TimeModel] = result.scalars().all()
        
        query = select(AtletaModel)
        result = await session.execute(query)
        atletas: List[AtletaModel] = result.scalars().all()
        
        query = select(ModalidadeModel)
        result = await session.execute(query)
        modalidades: List[ModalidadeModel] = result.scalars().all()
        
        for time in times:
            for modalidade in modalidades:
                if modalidade.id == time.modalidade_id:
                    time.modalidade = modalidade.nome
            
            for atleta in atletas:
                if time.jogador1 == atleta.id:
                    time.jogador1_nome = atleta.nome

            for atleta in atletas:
                if time.jogador2 == atleta.id:
                    time.jogador2_nome = atleta.nome 

            for atleta in atletas:
                if time.jogador3 == atleta.id:
                    time.jogador3_nome = atleta.nome 
                    
            for atleta in atletas:
                if time.jogador4 == atleta.id:
                    time.jogador4_nome = atleta.nome 

            for atleta in atletas:
                if time.jogador5 == atleta.id:
                    time.jogador5_nome = atleta.nome 
                    
            for atleta in atletas:
                if time.jogador6 == atleta.id:
                    time.jogador6_nome = atleta.nome 
                    
            for atleta in atletas:
                if time.jogador7 == atleta.id:
                    time.jogador7_nome = atleta.nome 
                    
            for atleta in atletas:
                if time.jogador8 == atleta.id:
                    time.jogador8_nome = atleta.nome 
                    
            for atleta in atletas:
                if time.jogador9 == atleta.id:
                    time.jogador9_nome = atleta.nome 
                    
            for atleta in atletas:
                if time.jogador10 == atleta.id:
                    time.jogador10_nome = atleta.nome          
       
        return times




    
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_time( id: int = Path(title="ID do time que deseja deletar", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TimeModel).where(TimeModel.id == id)
        result = await session.execute(query)
        time_del: List[TimeModel] = result.scalars().one_or_none()

        if time_del:
            await session.delete(time_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Time não encontrado", status_code=status.HTTP_404_NOT_FOUND)