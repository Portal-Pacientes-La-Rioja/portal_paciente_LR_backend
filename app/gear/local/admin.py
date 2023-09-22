from typing import List, Union, Optional

from sqlalchemy.orm import Session

from app.models.institutions import Institutions as model_institution
from app.models.person import Person as model_person
from app.models.user import User as model_user
from app.schemas.admin_status_enum import AdminStatusEnum
from app.schemas.persons import PersonsReduced, PersonUsername
from app.schemas.responses import ResponseNOK, ResponseOK
from app.schemas.returned_object import ReturnMessage
from app.schemas.user import CreateUserAdmin
from app.schemas.user import UserAdmin


def list_of_persons(only_accepted: bool, db: Session, username: Optional[str] = None):
    """
    Return list of persons, only name surname and if is accepted or
    not in the system.
    """
    admin_user: model_user = (
        db.query(model_user).where(model_user.username == username).first()
    )

    if not admin_user.is_admin:
        return []

    # A superadmin can query users from all institutions
    if admin_user.is_superadmin:
        cond_institution = True
    else:
        cond_institution = (
            model_person.id_usual_institution.in_(
                [inst.id for inst in admin_user.institutions]
            )
            if admin_user.institutions
            else True
        )

    if only_accepted is None:
        cond = True
    else:
        if only_accepted:
            cond = model_person.id_admin_status == AdminStatusEnum.validated.value
        else:
            cond = (
                model_person.id_admin_status == AdminStatusEnum.validation_pending.value
                or model_person.id_admin_status
                == AdminStatusEnum.validation_rejected.value
            )

    p_list = (
        db.query(
            model_person,
            model_person.id,
            model_person.surname,
            model_person.name,
            model_person.is_deleted,
            model_person.id_admin_status,
            model_person.id_person_status,
            model_person.id_usual_institution,
            model_user.username,
            model_person.inst_from_portal,
        )
        .join(model_user, model_user.id_person == model_person.id)
        .where(model_person.is_deleted == None)
        .where(cond)
        .where(cond_institution)
        .all()
    )

    persons_to_return = []

    for p in p_list:
        persons_to_return.append(
            PersonsReduced(
                id=p.id,
                username=p.username,
                name=p.name,
                surname=p.surname,
                id_admin_status=p.id_admin_status,
                id_person_status=p.id_person_status,
                id_usual_institution=p.id_usual_institution,
                inst_from_portal=p.inst_from_portal,
            )
        )
    return persons_to_return


def list_of_persons_accepted(db: Session):
    return list_of_persons(True, db)


def list_of_persons_to_accept(db: Session, username: Optional[str] = None):
    """
    Return list of persons, only name and surname of persons that
    need to be accepted.
    """
    all_people = list_of_persons(False, db, username)

    # Only returns persons peding to accept
    return [person for person in all_people if person.id_admin_status == 1]


def list_of_persons_in_general(db: Session, username: Optional[str] = None):
    """
    Return list of persons, without considering status.
    """
    return list_of_persons(None, db, username)


def accept_a_person(person_username: PersonUsername, db: Session):
    return change_person_status_by_admin(
        person_username, AdminStatusEnum.validated.value, db
    )


def not_accept_a_person(person_username: PersonUsername, db: Session):
    return change_person_status_by_admin(
        person_username, AdminStatusEnum.validation_rejected.value, db
    )


def change_person_status_by_admin(
    person_username: PersonUsername, admin_status_id: int, db: Session
):
    try:
        existing_user = (
            db.query(model_user)
            .where(model_user.username == person_username.username)
            .first()
        )

        if existing_user is not None:
            existing_person = (
                db.query(model_person)
                .where(model_person.id == existing_user.id_person)
                .first()
            )

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
        existing_user = (
            db.query(model_user)
            .where(model_user.username == person_username.username)
            .first()
        )

        if existing_user is not None:
            existing_person = (
                db.query(model_person)
                .where(model_person.id == existing_user.id_person)
                .first()
            )

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


def create_user_admin(user: CreateUserAdmin, db: Session):
    try:
        new_user = model_user(**user.dict(), id_person=0, id_user_status=0)
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


def assign_institutions_to_admins(
    username: str, institutions_ids: List[int], db: Session
):
    try:
        user = (
            db.query(model_user).where(model_user.username == username).one()
        )  # type: model_user
        if not user.admin:
            return ResponseNOK(message=f"Hey, {username} is not an Admin.", code=417)

        institutions = (
            db.query(model_institution)
            .filter(model_institution.id.in_(institutions_ids))
            .all()
        )
        user.institutions = institutions

        set_institutions_all = set(institutions_ids)
        set_institutions_saved = set(inst.id for inst in institutions)

        old_institutions = set_institutions_all - set_institutions_saved

        user.old_institutions = list(old_institutions)

        db.commit()

    except Exception as err:
        print(err)
        db.rollback()
        return ResponseNOK(message="Something wrong.", code=417)

    return ResponseOK(message="The institutions was added successfully.", code=201)


def list_of_admins(db: Session):
    try:
        users = db.query(model_user).where(model_user.is_admin == 1).all()
    except Exception as err:
        print(err)
        db.rollback()
        return ResponseNOK(message="Something wrong.", code=417)
    return [UserAdmin.from_orm(user) for user in users]


def get_admin_by_id(user_id: int, db: Session):
    try:
        users = (
            db.query(model_user)
            .where((model_user.id == user_id) & (model_user.is_admin == 1))
            .all()
        )
    except Exception as err:
        print(err)
        db.rollback()
        return ResponseNOK(message="Something wrong.", code=417)
    return [UserAdmin.from_orm(user) for user in users]


def on_off_admin(user_id: int, db: Session):
    try:
        existing_admin = (
            db.query(model_user)
            .where((model_user.id == user_id) & (model_user.is_admin == 1))
            .first()
        )
        if existing_admin.super_admin:
            return ResponseNOK(message="What are you trying to do? ;-)", code=417)
        # swap to 1 or 0 according its value
        existing_admin.is_admin_activate = existing_admin.is_admin_activate ^ 1
        db.commit()
    except Exception as e:
        db.rollback()
        # self.log.log_error_message(e, self.module)  TODO: fix this
        return ResponseNOK(message="Admin does not updated.", code=417)

    return ResponseOK(message="Updated successfully.", code=201)


def change_password(
    admin: CreateUserAdmin, db: Session
) -> Union[ResponseOK, ResponseNOK]:
    try:
        existing_admin = (
            db.query(model_user)
            .where((model_user.username == admin.username) & (model_user.is_admin == 1))
            .first()
        )
        if existing_admin is None:
            return ResponseOK(
                message="Something Wrong.",
                code=417,
            )
        existing_admin.new_password(admin.password)
        db.commit()

        return ResponseOK(
            value=str(existing_admin.id),
            message="Password changed successfully.",
            code=201,
        )

    except Exception as e:
        db.rollback()
        # log.log_error_message(e, self.module)
        print(e)  # TODO: fix logger
        return ResponseNOK(message="Person cannot be updated.", code=417)
