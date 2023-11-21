from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.gear.local.local_impl import LocalImpl
from app.main import get_db
from app.routes.common import router_institutions
from app.schemas.institutions import Institution as schemas_institution
from app.schemas.institutions import InstitutionWithID as schemas_institution_with_id
from app.schemas.responses import ResponseOK, ResponseNOK


@router_institutions.put(
    "/onoffinstitution",
    responses={417: {"model": ResponseNOK}},
    tags=["Institutions"],
)
async def update(institution: schemas_institution, db: Session = Depends(get_db)):
    return LocalImpl(db).on_off_institution(institution)


@router_institutions.put(
    "/updateinstitution",
    response_model=ResponseOK,
    responses={417: {"model": ResponseNOK}},
    tags=["Institutions"],
)
async def update(institution: schemas_institution, db: Session = Depends(get_db)):
    return LocalImpl(db).update_institution(institution)


@router_institutions.get(
    "/getinstitutionsbyid",
    response_model=schemas_institution,
    responses={417: {"model": ResponseNOK}},
    tags=["Institutions"],
)
async def get_institution_by_id(institution_id: int, db: Session = Depends(get_db)):
    institution = LocalImpl(db).get_institutions_by_id(institution_id)
    return institution


@router_institutions.get(
    "/getinstitutions",
    response_model=List[schemas_institution_with_id],
    responses={417: {"model": ResponseNOK}},
    tags=["Institutions"],
)
async def get_institution(db: Session = Depends(get_db)):
    return LocalImpl(db).get_institutions()


@router_institutions.post(
    "/createinstitution",
    response_model=ResponseOK,
    responses={417: {"model": ResponseNOK}},
    tags=["Institutions"],
)
async def create_institution(institution: schemas_institution, db: Session = Depends(get_db)):
    return LocalImpl(db).create_institution(institution)


@router_institutions.get("/allWithNewData", tags=["Institutions"])
async def all_institutions(db: Session = Depends(get_db)):
    institutions = LocalImpl(db).get_merge_institutions()

    return [{"id": institution.id, "name": institution.name}
            for institution in institutions]
