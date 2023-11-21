from app.config.config import (
    API_DATOS_GOB_AR_PROVINCIAS,
    API_DATOS_GOB_AR_DEPARTAMENTOS,
    API_DATOS_GOB_AR_LOCALIDADES
)
import requests
import urllib
from typing import List, Dict
from itertools import chain


PARAMS = {
    "orden": "nombre",
    "aplanar": True,
    "campos": "basico",
    "max": 100,
    "exacto": True
}


def get_all_provincias() -> List[Dict[str, str]]:
    url = "{}?{}".format(API_DATOS_GOB_AR_PROVINCIAS, urllib.parse.urlencode(PARAMS))
    return requests.get(url).json()["provincias"]


def get_all_departamentos_from(provincia_id: str) -> List[Dict[str, str]]:
    params = dict(chain.from_iterable(d.items() for d in (PARAMS, {"provincia": provincia_id})))
    url = "{}?{}".format(API_DATOS_GOB_AR_DEPARTAMENTOS, urllib.parse.urlencode(params))
    return requests.get(url).json()["departamentos"]


def get_all_localidades_from(departamento_id: str) -> List[Dict[str, str]]:
    params = dict(chain.from_iterable(d.items() for d in (PARAMS, {"departamento": departamento_id})))
    url = "{}?{}".format(API_DATOS_GOB_AR_LOCALIDADES, urllib.parse.urlencode(params))
    return requests.get(url).json()["localidades"]


def get_provincia_name(provincia_id: str) -> Dict[str, str]:
    return {
        "nombre": provincia["nombre"]
        for provincia in get_all_provincias()
        if provincia["id"] == provincia_id
    }


def get_departamento_name(provincia_id: str, departamento_id: str) -> Dict[str, str]:
    return {
        "nombre": departamento["nombre"]
        for departamento in get_all_departamentos_from(provincia_id)
        if departamento["id"] == departamento_id
    }


def get_localidad_name(departamento_id: str, localidad_id: str) -> Dict[str, str]:
    return {
        "nombre": localidad["nombre"]
        for localidad in get_all_localidades_from(departamento_id)
        if localidad["id"] == localidad_id
    }
