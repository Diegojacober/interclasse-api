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
                             )
    
    db.add(novo_time)
    await db.commit()
    return "Adicionado"


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
        
        
        return times



# #GET atleta
# @router.get('/{id}', response_model=List[AtletaSchema])
# async def get_atletas(id: int = Path(title="ID do atleta desejado", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(AtletaModel).where(AtletaModel.id == id)
#         result = await session.execute(query)
#         atletas: List[AtletaModel] = result.scalars().all()
        
#         query = select(CursoModel)
#         result = await session.execute(query)
#         cursos: List[CursoModel] = result.scalars().all()
        
#         query = select(ModalidadeModel)
#         result = await session.execute(query)
#         modalidades: List[ModalidadeModel] = result.scalars().all()
        
#         for atleta in atletas:
#             for curso in cursos:
#                 if curso.id == atleta.curso_id:
#                    atleta.curso = curso.curso
                   
#             for modalidade in modalidades:
#                 if modalidade.id == atleta.modalidade_id:
#                     atleta.modalidade = modalidade.nome
                   
#         return atletas
    
    
# #GET atleta by face_url
# @router.get('/face/{url_face}', response_model=List[AtletaSchema], description="Get atleta by face url")
# async def get_atletas(url_face: str = Path(title="url do atleta desejado", description="Deve ser a url unica da face do atleta"), db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(AtletaModel).where(AtletaModel.face_url == url_face)
#         result = await session.execute(query)
#         atletas: List[AtletaModel] = result.scalars().all()
        
#         query = select(CursoModel)
#         result = await session.execute(query)
#         cursos: List[CursoModel] = result.scalars().all()
        
#         query = select(ModalidadeModel)
#         result = await session.execute(query)
#         modalidades: List[ModalidadeModel] = result.scalars().all()
        
#         for atleta in atletas:
#             for curso in cursos:
#                 if curso.id == atleta.curso_id:
#                    atleta.curso = curso.curso
                   
#             for modalidade in modalidades:
#                 if modalidade.id == atleta.modalidade_id:
#                     atleta.modalidade = modalidade.nome
                   
#         return atletas
    
    
# @router.put('/{id}', response_model=AtletaSchema, status_code=status.HTTP_202_ACCEPTED)
# async def put_atleta(atleta: AtletaSchema, id: int = Path(title="ID do atleta que deseja atualizar", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(AtletaModel).where(AtletaModel.id == id)
#         result = await session.execute(query)
#         atleta_up: List[AtletaModel] = result.scalars().one_or_none()

#         if atleta_up:
            
#             atleta_up.face_url = atleta_up.face_url if atleta.face_url == None else atleta.face_url 
#             atleta_up.curso_id = atleta.curso_id
#             atleta_up.idade = atleta.idade
#             atleta_up.modalidade_id = atleta.modalidade_id
#             atleta_up.nome = atleta.nome
            
#             await session.commit()
#             return atleta_up
#         else:
#             raise HTTPException(detail="Atleta não encontrado", status_code=status.HTTP_404_NOT_FOUND)


    
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_atleta( id: int = Path(title="ID do atleta que deseja deletar", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(AtletaModel).where(AtletaModel.id == id)
#         result = await session.execute(query)
#         atleta_del: List[AtletaModel] = result.scalars().one_or_none()

#         if atleta_del:
#             await session.delete(atleta_del)
#             await session.commit()

#             return Response(status_code=status.HTTP_204_NO_CONTENT)
#         else:
#             raise HTTPException(detail="Atleta não encontrado", status_code=status.HTTP_404_NOT_FOUND)