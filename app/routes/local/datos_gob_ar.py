from app.gear.datos_gob_ar.datos_gob_ar import (
    get_all_localidades_from,
    get_all_departamentos_from,
    get_all_provincias
)
from app.routes.common import router_datos
from app.schemas.responses import ResponseNOK


@router_datos.get(
    "/get_all_provincias",
    responses={417: {"model": ResponseNOK}},
    tags=["Datos"],
)
async def get_provincias():
    return get_all_provincias()


@router_datos.get(
    "/get_all_departamentos_from",
    responses={417: {"model": ResponseNOK}},
    tags=["Datos"],
)
async def get_departamentos(provincias_id: str):
    return get_all_departamentos_from(provincias_id)


@router_datos.get(
    "/get_all_localidades_from",
    responses={417: {"model": ResponseNOK}},
    tags=["Datos"],
)
async def get_localidades(departamento_id: str):
    return get_all_localidades_from(departamento_id)
