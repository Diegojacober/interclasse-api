from fastapi import APIRouter

from api.v1.endpoints import curso, modalidade, atleta, time, jogo,campeao

api_router = APIRouter()

api_router.include_router(curso.router, prefix='/cursos', tags=['Rotas dos cursos'])
api_router.include_router(modalidade.router, prefix='/modalidades', tags=['Rotas das modalidades'])
api_router.include_router(atleta.router, prefix='/atletas', tags=['Rotas dos atletas'])
api_router.include_router(time.router, prefix='/times', tags=['Rotas dos times'])
api_router.include_router(jogo.router, prefix='/jogos', tags=['Rotas dos jogos'])
api_router.include_router(campeao.router, prefix='/campeao', tags=['Rotas dos campeões'])
