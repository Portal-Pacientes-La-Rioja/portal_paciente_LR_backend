from app.gear.local.sumar import get_afiliado_data
from app.routes.common import router_sumar
from app.schemas.sumar_result import SumarResult
from app.gear.local.sumar import SumarImpl
from typing import Optional

sumar_impl = SumarImpl()

@router_sumar.get("/data/{dni_afiliado}", tags=["SUMAR", "data"], response_model=SumarResult)
async def get_sumar_data(dni_afiliado: str) -> SumarResult:
    return get_afiliado_data(dni_afiliado)

@router_sumar.get("/ceb/{dni_afiliado}", tags=["SUMAR", "ceb"], response_model=Optional[str])
async def get_ceb_value(dni_afiliado: str) -> Optional[str]:
    ceb_value = sumar_impl.get_ceb_value(dni_afiliado)
    return ceb_value

