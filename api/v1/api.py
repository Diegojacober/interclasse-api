from fastapi import APIRouter

from api.v1.endpoints import curso, modalidade, atleta

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=['Rotas dos cursos'])
api_router.include_router(modalidade.router, prefix='/modalidades', tags=['Rotas das modalidades'])
api_router.include_router(atleta.router, prefix='/atletas', tags=['Rotas dos atletas'])


#api/v1/cursos