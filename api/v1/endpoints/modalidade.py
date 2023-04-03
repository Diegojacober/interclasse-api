from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import Path

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.modalidades import ModalidadeModel
from schemas.modalidades_schema import ModalidadeSchema
from core.deps import get_session


router = APIRouter()

#POST modalidade
@router.post("/", status_code=status.HTTP_201_CREATED, response_model= ModalidadeSchema)
async def post_modalidade(modalidade: ModalidadeSchema, db: AsyncSession = Depends(get_session)):
    nova_modalidade = ModalidadeModel(nome=modalidade.nome,
                                      duo=modalidade.duo,
                                      team=modalidade.team,
                                      individual=modalidade.individual)

    db.add(nova_modalidade)
    await db.commit()

    return nova_modalidade

#GET modalidades
@router.get('/', response_model=List[ModalidadeSchema])
async def get_modalidades(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ModalidadeModel)
        result = await session.execute(query)
        modalidades: List[ModalidadeModel] = result.scalars().all()

        return modalidades

#GET modalidade
@router.get('/{id}', response_model=ModalidadeSchema)
async def get_modalidade(id: int = Path(title="ID da modalidade desejada", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
    async with db as session:

        query = select(ModalidadeModel).where(ModalidadeModel.id == id)
        result = await session.execute(query)
        modalidade: ModalidadeModel = result.scalars().one_or_none()

        if modalidade:
            return modalidade
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=status.HTTP_404_NOT_FOUND)

#PUT modalidade
@router.put('/{id}', response_model=ModalidadeSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_modalidade(modalidade: ModalidadeSchema, id: int = Path(title="ID da modalidade que deseja atualizar", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ModalidadeModel).where(ModalidadeModel.id == id)
        result = await session.execute(query)
        modalidade_up: List[ModalidadeModel] = result.scalars().one_or_none()

        if modalidade_up:
            modalidade_up.nome = modalidade.nome

            await session.commit()

            return modalidade_up
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=status.HTTP_404_NOT_FOUND)

#DELETE modalidade
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_modalidade( id: int = Path(title="ID da modalidade que deseja deletar", description="Deve ser maior que 0", gt=0), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ModalidadeModel).where(ModalidadeModel.id == id)
        result = await session.execute(query)
        modalidade_del: List[ModalidadeModel] = result.scalars().one_or_none()

        if modalidade_del:
            await session.delete(modalidade_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=status.HTTP_404_NOT_FOUND)