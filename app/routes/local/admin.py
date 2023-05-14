from typing import List, Union

from fastapi import Depends
from sqlalchemy.orm import Session

from app.gear.local.admin import (
    remove_a_person,
    not_accept_a_person,
    accept_a_person,
    list_of_persons_to_accept,
    list_of_persons_accepted,
    list_of_persons_in_general,
    create_user_admin
)
from app.main import get_db
from app.routes.common import router_admin
from app.schemas.persons import PersonUsername, PersonsReduced
from app.schemas.responses import ResponseOK, ResponseNOK
from app.schemas.returned_object import ReturnMessage
from app.schemas.user import UserAdmin


@router_admin.delete("/person", name="Remove a Person",
                     response_model=ReturnMessage, description="Remove a Person from the system")
async def delete_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return remove_a_person(person_username, db)


@router_admin.put("/notaccept", name="Deny access to a Person",
                  response_model=ReturnMessage, description="Denied access to a person")
async def not_accept_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return not_accept_a_person(person_username, db)


@router_admin.put("/id_admin_status", name="Accept a Person",
                  response_model=ReturnMessage, description="Accept a Person in the system")
async def accept_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return accept_a_person(person_username, db)


@router_admin.get("/persons_accepted", name="List of id_admin_status Person", response_model=List[PersonsReduced], description="List of Persons id_admin_status in the system")
async def persons_accepted(db: Session = Depends(get_db)):
    return list_of_persons_accepted(db)


@router_admin.get("/persons_to_be_accepted", name="List of id_admin_status Person", response_model=List[PersonsReduced], description="List of Persons to be id_admin_status in the system")
async def persons_accepted(db: Session = Depends(get_db)):
    return list_of_persons_to_accept(db)


@router_admin.get("/persons", name= "List of persons", response_model=List[PersonsReduced], description="List of all Persons in the system")
async def persons(db: Session = Depends(get_db)):
    return list_of_persons_in_general(db)

# TODO add response model
@router_admin.post("/create_admin",
                   # name="Create an user admin",  # Check this, is not recognized by the method user_is_authorized2
                   description="Create an user admin",
                   response_model=Union[ResponseOK, ResponseNOK]
                  )
async def create_admin(user: UserAdmin, db: Session = Depends(get_db)):
    return create_user_admin(user, db)
