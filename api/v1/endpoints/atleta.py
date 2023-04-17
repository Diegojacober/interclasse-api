from typing import List

from fastapi import APIRouter
from fastapi import status, UploadFile
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import Path

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.atletas import AtletaModel
from models.cursos import CursoModel
from models.modalidades import ModalidadeModel
from schemas.atletas_schema import AtletaSchema
from core.deps import get_session
import os
from azure.storage.blob import BlobServiceClient

router = APIRouter()

#POST atleta
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AtletaSchema)
async def post_atleta(atleta: AtletaSchema, db: AsyncSession = Depends(get_session)):


    novo_atleta = AtletaModel(nome=atleta.nome,
                              idade=atleta.idade,
                              face_url=atleta.face_url,
                              curso_id=atleta.curso_id,
                              modalidade_id=atleta.modalidade_id)
    db.add(novo_atleta)
    await db.commit()

    return novo_atleta


#GET atletas
@router.get('/', response_model=List[AtletaSchema])
async def get_atletas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AtletaModel)
        result = await session.execute(query)
        atletas: List[AtletaModel] = result.scalars().all()
        
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        
        query = select(ModalidadeModel)
        result = await session.execute(query)
        modalidades: List[ModalidadeModel] = result.scalars().all()
        
        for atleta in atletas:
            for curso in cursos:
                if curso.id == atleta.curso_id:
                   atleta.curso = curso.curso
                   
            for modalidade in modalidades:
                if modalidade.id == atleta.modalidade_id:
                    atleta.modalidade = modalidade.nome
                   
        return atletas

@router.post('/upload', status_code=status.HTTP_201_CREATED)
async def upload_image(image: UploadFile):
    strorage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=imagensinterclasse;AccountKey=BM/mVQXYFVf6gWn2k0Xd9Fj+jCbEv7C4nh/slDBcdMxgITFFHnpUuCYSSr+jdQkqxfcmziPllMy4+ASt95owUQ==;EndpointSuffix=core.windows.net'

    blob_service_client = BlobServiceClient.from_connection_string(strorage_connection_string)
    container_name = 'isimagefolder'
    
    blob_obj = blob_service_client.get_blob_client(container=container_name, blob=image.filename)        

    with open(image.filename, 'wb') as f:
        contents = await image.read()
        f.write(contents)
        blob_obj.upload_blob(contents)

    return {"filename": image.filename, "content_type": image.content_type}