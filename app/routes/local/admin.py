from typing import List, Union

from app.auth.auth import get_current_user
from app.gear.local.admin import (
    accept_a_person,
    assign_institutions_to_admins,
    change_password,
    create_user_admin,
    get_admin_by_id,
    list_of_admins,
    list_of_persons_accepted,
    list_of_persons_in_general,
    list_of_persons_to_accept,
    not_accept_a_person,
    on_off_admin,
    remove_a_person,
    list_persons_family_group_to_accept,
)
from app.main import get_db
from app.routes.common import router_admin
from app.schemas.persons import PersonsReduced, PersonUsername
from app.schemas.responses import ResponseNOK, ResponseOK
from app.schemas.returned_object import ReturnMessage
from app.schemas.user import CreateUserAdmin, UserAdmin
from fastapi import Depends
from sqlalchemy.orm import Session

# from fastapi_pagination import Page


@router_admin.delete(
    "/person",
    name="Remove a Person",
    response_model=ReturnMessage,
    description="Remove a Person from the system",
)
async def delete_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return remove_a_person(person_username, db)


@router_admin.put(
    "/notaccept",
    name="Deny access to a Person",
    response_model=ReturnMessage,
    description="Denied access to a person",
)
async def not_accept_person(
    person_username: PersonUsername, db: Session = Depends(get_db)
):
    return not_accept_a_person(person_username, db)


@router_admin.put(
    "/id_admin_status",
    name="Accept a Person",
    response_model=ReturnMessage,
    description="Accept a Person in the system",
)
async def accept_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return accept_a_person(person_username, db)


@router_admin.get(
    "/persons_accepted",
    name="List of id_admin_status Person",
    response_model=List[PersonsReduced],
    description="List of Persons id_admin_status in the system",
)
async def persons_accepted(db: Session = Depends(get_db)):
    return list_of_persons_accepted(db)


@router_admin.get(
    "/persons_to_be_accepted",
    name="List of perstons to be accepted",
    response_model=List[PersonsReduced],
    description="List of Persons to be id_admin_status in the system",
)
async def persons_to_accept(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    return list_of_persons_to_accept(db, current_user)


@router_admin.get(
    "/relatives_to_accept",
    name="List of relatives to be accepted",
    response_model=List[PersonsReduced],
    description="List of relatives to be id_admin_status in the system",
)
async def relatives_to_accept(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    return list_persons_family_group_to_accept(db, current_user)


@router_admin.get(
    "/persons",
    name="List of persons",
    response_model=List[PersonsReduced],
    description="List of all Persons in the system",
)
async def persons(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    return list_of_persons_in_general(db, current_user)


# TODO add response model
@router_admin.post(
    "/create_admin",
    # name="Create a user admin",  # Check this, is not recognized by the method user_is_authorized2
    description="Create an user admin",
    response_model=Union[ResponseOK, ResponseNOK],
)
async def create_admin(user: CreateUserAdmin, db: Session = Depends(get_db)):
    return create_user_admin(user, db)


@router_admin.put(
    "/assign_institutions",
    # name="Create a user admin",  # Check this, is not recognized by the method user_is_authorized2
    description="Assign institutions to Admins",
    response_model=Union[ResponseOK, ResponseNOK],
)
async def create_admin(
    username: str, institutions_ids: List[int], db: Session = Depends(get_db)
):
    return assign_institutions_to_admins(username, institutions_ids, db)


@router_admin.get(
    "/admins",
    # name="Create a user admin",  # Check this, is not recognized by the method user_is_authorized2
    description="List of Admins",
    response_model=Union[List[UserAdmin], ResponseNOK],
)
async def list_admins(db: Session = Depends(get_db)):
    return list_of_admins(db)


@router_admin.get(
    "/adminbyid",
    # name="Create an user admin",  # Check this, is not recognized by the method user_is_authorized2
    description="Get Admin by id",
    response_model=Union[List[UserAdmin], ResponseNOK],
)
async def list_admin_id(user_id: int, db: Session = Depends(get_db)):
    return get_admin_by_id(user_id, db)


@router_admin.put(
    "/onoffadmin",
    # name="Create an user admin",  # Check this, is not recognized by the method user_is_authorized2
    description="Activate/deactivate admin",
    response_model=Union[ResponseOK, ResponseNOK],
)
async def onoff_user_admin(user_id: int, db: Session = Depends(get_db)):
    return on_off_admin(user_id, db)


@router_admin.put(
    "/change_password",
    # name="Create an user admin",  # Check this, is not recognized by the method user_is_authorized2
    description="change the password to an admin",
    response_model=Union[ResponseOK, ResponseNOK],
)
async def change_password_admin(admin: CreateUserAdmin, db: Session = Depends(get_db)):
    return change_password(admin, db)
