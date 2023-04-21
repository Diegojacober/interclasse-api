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
from models.pesquisas import ImageSearchModel
from models.jogos import JogoModel
from models.times import TimeModel
from schemas.atletas_schema import AtletaSchema
from schemas.pesquisa_schema import ImageSearchSchema
from schemas.times_schema import TimeSchema
from core.deps import get_session
import os, datetime
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
    
#GET atletas
@router.get('/modalidade/{id_modalidade}', response_model=List[AtletaSchema])
async def get_atletas(id_modalidade:int,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AtletaModel).where(AtletaModel.modalidade_id == id_modalidade)
        result = await session.execute(query)
        atletas: List[AtletaModel] = result.scalars().fetchall()
        
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        
                   
        for atleta in atletas:
            for curso in cursos:
                if curso.id == atleta.curso_id:
                   atleta.curso = curso.curso
                   
        return atletas
    
@router.get('/ultimapesquisa', response_model=AtletaSchema)
async def get_last_search(db: AsyncSession = Depends(get_session)):    
    async with db as session:
        query = select(ImageSearchModel).order_by(ImageSearchModel.id.desc())
        result = await session.execute(query)
        last_record: ImageSearchModel = result.scalars().first()
        
        query = select(AtletaModel).where(AtletaModel.face_url == last_record.nome_imagem)
        result = await session.execute(query)
        atleta: AtletaModel = result.scalars().one_or_none()
        
        query = select(CursoModel).where(CursoModel.id == atleta.curso_id)
        result = await session.execute(query)
        curso: CursoModel = result.scalars().one_or_none()
        
        atleta.curso = curso.curso
        
        query = select(ModalidadeModel).where(ModalidadeModel.id == atleta.modalidade_id)
        result = await session.execute(query)
        modalidade: ModalidadeModel = result.scalars().one_or_none()
        
        atleta.modalidade = modalidade.nome
        
        query = select(TimeModel).where((TimeModel.jogador1 == atleta.id) | (TimeModel.jogador2 == atleta.id) |
                                        (TimeModel.jogador2 == atleta.id) | (TimeModel.jogador3 == atleta.id) |
                                        (TimeModel.jogador4 == atleta.id) | (TimeModel.jogador5 == atleta.id) |
                                        (TimeModel.jogador6 == atleta.id) | (TimeModel.jogador7 == atleta.id) |
                                        (TimeModel.jogador8 == atleta.id) | (TimeModel.jogador9 == atleta.id) | (TimeModel.jogador10 == atleta.id))
        
        result = await session.execute(query)
        time: TimeModel = result.scalars().one_or_none()
        
        data_e_hora_atual = str(datetime.datetime.now())[0:11]
        
        #mandante
        query = select(JogoModel).where((JogoModel.data_do_jogo >= data_e_hora_atual)).where(JogoModel.time1 == time.id)
        result = await session.execute(query)
        jogos: JogoModel = result.scalars().fetchall()
        
        lista_jogos = []
        for jogo in jogos:
            query = select(TimeModel).where(TimeModel.id == jogo.time1)
            result = await session.execute(query)
            time1: TimeModel = result.scalars().one_or_none()
            jogo.time1_nome = time1.nome
            
            query = select(TimeModel).where(TimeModel.id == jogo.time2)
            result = await session.execute(query)
            time1: TimeModel = result.scalars().one_or_none()
            jogo.time2_nome = time1.nome

            
            jogo_dict = {"time1": jogo.time1_nome, "time2":jogo.time2_nome,"data_do_jogo": jogo.data_do_jogo}
            lista_jogos.append(jogo_dict.copy())
            
        atleta.proximos_jogos = lista_jogos.copy()
        
        #visantante
        query = select(JogoModel).where((JogoModel.data_do_jogo >= data_e_hora_atual)).where(JogoModel.time2 == time.id)
        result = await session.execute(query)
        jogos: JogoModel = result.scalars().fetchall()
        
        lista_jogos = []
        for jogo in jogos:
            query = select(TimeModel).where(TimeModel.id == jogo.time1)
            result = await session.execute(query)
            time1: TimeModel = result.scalars().one_or_none()
            jogo.time1_nome = time1.nome
            
            query = select(TimeModel).where(TimeModel.id == jogo.time2)
            result = await session.execute(query)
            time1: TimeModel = result.scalars().one_or_none()
            jogo.time2_nome = time1.nome

            
            jogo_dict = {"time1": jogo.time1_nome, "time2":jogo.time2_nome,"data_do_jogo": jogo.data_do_jogo}
            lista_jogos.append(jogo_dict.copy())
            
        atleta.proximos_jogos += lista_jogos.copy()
        
        
        
    return atleta


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

@router.post('/searchimage',status_code=status.HTTP_201_CREATED, response_model=ImageSearchSchema)
async def create_search_now(dados: ImageSearchSchema,db: AsyncSession = Depends(get_session)):
    data_e_hora_atual = str(datetime.datetime.now())[0:19]
    
    nova_pesquisa = ImageSearchModel(nome_imagem=dados.nome_imagem,horario=data_e_hora_atual)
    db.add(nova_pesquisa)
    await db.commit()

    return nova_pesquisa
