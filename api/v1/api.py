from fastapi import APIRouter

from api.v1.endpoints import curso, modalidade

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=['Rotas dos cursos'])
api_router.include_router(modalidade.router, prefix='/modalidades', tags=['Rotas das modalidades'])

#api/v1/cursos