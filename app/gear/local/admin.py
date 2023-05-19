from typing import List

from sqlalchemy.orm import Session
from app.models.institutions import Institutions as model_institution

from app.models.person import Person as model_person
from app.models.user import User as model_user
from app.schemas.admin_status_enum import AdminStatusEnum
from app.schemas.persons import PersonsReduced, PersonUsername
from app.schemas.responses import ResponseNOK, ResponseOK
from app.schemas.returned_object import ReturnMessage
from app.schemas.user import UserAdmin


def list_of_persons(only_accepted: bool, db: Session):
    """
    Return list of persons, only name surname and if is accepted or
    not in the system.
    """

    if only_accepted is None:
        cond = True
    else:
        if only_accepted:
            cond = model_person.id_admin_status == AdminStatusEnum.validated.value
        else:
            cond = (model_person.id_admin_status == AdminStatusEnum.validation_pending.value
                    or model_person.id_admin_status == AdminStatusEnum.validation_rejected.value)

    p_list = db.query(model_person,
                      model_person.id,
                      model_person.surname,
                      model_person.name,
                      model_person.is_deleted,
                      model_person.id_admin_status,
                      model_person.id_person_status,
                      model_person.id_usual_institution,
                      model_user.username,
                      model_person.inst_from_portal)\
        .join(model_user, model_user.id_person == model_person.id) \
        .where(model_person.is_deleted == None) \
        .where(cond) \
        .all()

    persons_to_return = []

    for p in p_list:
        persons_to_return.append(PersonsReduced(id=p.id,
                                                username=p.username,
                                                name=p.name,
                                                surname=p.surname,
                                                id_admin_status=p.id_admin_status,
                                                id_person_status=p.id_person_status,
                                                id_usual_institution=p.id_usual_institution,
                                                inst_from_portal=p.inst_from_portal))
    return persons_to_return


def list_of_persons_accepted(db: Session):
    return list_of_persons(True, db)


def list_of_persons_to_accept(db: Session):
    """
    Return list of persons, only name and surname of persons that
    need to be accepted.
    """
    return list_of_persons(False, db)


def list_of_persons_in_general(db: Session):
    """
    Return list of persons, without considering status.
    """
    return list_of_persons(None, db)


def accept_a_person(person_username: PersonUsername, db: Session):
    return change_person_status_by_admin(person_username, AdminStatusEnum.validated.value, db)


def not_accept_a_person(person_username: PersonUsername, db: Session):
    return change_person_status_by_admin(person_username, AdminStatusEnum.validation_rejected.value, db)


def change_person_status_by_admin(person_username: PersonUsername, admin_status_id: int, db: Session):
    try:
        existing_user = db.query(model_user).where(model_user.username == person_username.username).first()

        if existing_user is not None:
            existing_person = db.query(model_person).where(model_person.id == existing_user.id_person).first()

            if existing_person is not None:
                existing_person.id_admin_status = admin_status_id
                db.commit()
            else:
                return ReturnMessage(message="Nonexistent person.", code=417)
        else:
            return ReturnMessage(message="Nonexistent user.", code=417)

    except Exception:
        db.rollback()
        return ReturnMessage(message="Person cannot be updated.", code=417)

    return ReturnMessage(message="Person updated successfully.", code=201)


def remove_a_person(person_username: PersonUsername, db: Session):
    try:
        existing_user = db.query(model_user).where(model_user.username == person_username.username).first()

        if existing_user is not None:
            existing_person = db.query(model_person).where(model_person.id == existing_user.id_person).first()

            if existing_person is not None:
                existing_person.is_deleted = True
                db.commit()
            else:
                return ReturnMessage(message="Nonexistent person.", code=417)
        else:
            return ReturnMessage(message="Nonexistent user.", code=417)

    except Exception:
        db.rollback()
        return ReturnMessage(message="Person cannot be updated.", code=417)

    return ReturnMessage(message="Person updated successfully.", code=201)


def create_user_admin(user: UserAdmin, db: Session):
    try:
        new_user = model_user(**user.dict())
        # This method create only admin users
        new_user.is_admin = 1

        db.add(new_user)
        db.commit()
    except Exception as e:
        db.rollback()
        # TODO: Activate log
        # log.log_error_message(e, __file__)
        print(e)
        return ResponseNOK(message="User not created.", code=417)
    return ResponseOK(message="User created successfully.", code=201)


def assign_institutions_to_admins(username: str, institutions_ids: List[int], db: Session):
    try:
        user = db.query(model_user).where(model_user.username == username).one()  # type: model_user
        if not user.admin:
            return ResponseNOK(message=f"Hey, {username} is not an Admin.", code=417)

        institutions = db.query(model_institution).filter(model_institution.id.in_(institutions_ids)).all()
        user.institutions = institutions
        db.commit()

    except Exception as err:
        print(err)
        db.rollback()
        return ResponseNOK(message="Something wrong.", code=417)

    return ResponseOK(message="The institutions was added successfully.", code=201)