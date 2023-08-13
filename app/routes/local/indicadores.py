from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.gear.local.local_impl import LocalImpl
from app.main import get_db
from app.schemas.responses import ResponseOK, ResponseNOK
from app.routes.common import router_indicadores


###################CHACO#######################

@router_indicadores.get(
"/indicador_usuarios_activos",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)

async def indicador_usuarios_activos(db: Session = Depends(get_db)):
    contador = LocalImpl(db).indicador_usuarios_activos()
    return contador


@router_indicadores.get(
"/indicador_usuarios_master",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)
async def indicador_usuarios_master(db: Session = Depends(get_db)):
    contador = LocalImpl(db).indicador_usuarios_master()
    return contador


@router_indicadores.get(
"/indicador_grupo_familiar",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)
async def indicador_grupo_familiar(db: Session = Depends(get_db)):
    result = LocalImpl(db).indicador_grupo_familiar()
    return result
###################################################################

@router_indicadores.get(
"/indicador_cantidad_usuarios",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)
async def indicador_grupo_familiar(db: Session = Depends(get_db)):
    result = LocalImpl(db).indicador_cantidad_usuarios()
    return result

@router_indicadores.get(
"/indicador_usuarios_validados",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)
async def indicador_grupo_familiar(db: Session = Depends(get_db)):
    result = LocalImpl(db).indicador_usuarios_validados()
    return result
    

@router_indicadores.get(
"/indicador_usuarios_recazados",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)
async def indicador_grupo_familiar(db: Session = Depends(get_db)):
    result = LocalImpl(db).indicador_usuarios_rechazados()
    return result

@router_indicadores.get(
"/indicador_usuarios_pendientes",
responses={417: {"model": ResponseNOK}},
tags=["Indicadores"],
)
async def indicador_grupo_familiar(db: Session = Depends(get_db)):
    result = LocalImpl(db).indicador_usuarios_pendientes()
    return result


