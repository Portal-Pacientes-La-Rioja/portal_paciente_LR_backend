import re

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.routing import Match

from app.config.config import DEBUG_ENABLED
from app.config.database import Base, SessionLocal
from app.models.role_permission import RolePermission
from app.models.user import User
from app.models.user_role import UserRole


ADMIN_ROUTES = [
    "create_message",
    "update_message",
    "delete_message",
    "send_message",
    "Deny access to a Person",
    "Accept a Person",
    "Get Admin by id",
    "adminbyid",
    "List of persons",
    "get_admin_status",
    "List of perstons to be accepted",
    "persons_to_be_accepted",
    "relatives_to_accept",
    "List of relatives to be accepted",
    "set_admin_status_to_person",
]

SUPERADMIN_ROUTES = [
    "create_message",
    "update_message",
    "delete_message",
    "send_message",
    "set_admin_status_to_person",
    "get_admin_status",
    "Remove a Person",
    "Deny access to a Person",
    "Accept a Person",
    "List of id_admin_status Person",
    "List of persons",
    "Create an user admin",
    "create_admin",
    "assign_institutions",
    "admins",
    "adminbyid",
    "onoffadmin",
    "change_password_admin",
    "List of perstons to be accepted",
    "persons_to_be_accepted",
    "relatives_to_accept",
    "List of relatives to be accepted",
    "set_admin_status_to_person",
]


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    url = Column(String(1000), nullable=False)
    method = Column(String(10), nullable=False)

    @staticmethod
    def user_is_authorized(username: str, path: str, method: str) -> bool:
        db: Session = SessionLocal()

        permissions = (
            db.query(Permission)
            .join(RolePermission, RolePermission.id == RolePermission.id_permission)
            .join(UserRole, RolePermission.id_role == UserRole.id_role)
            .join(User, UserRole.id_user == User.id and User.username == username)
            .all()
        )

        db.close()

        for permission in permissions:
            patterns = [permission.url]
            pattern = "(?:% s)" % "|".join(patterns)
            if re.match(pattern, path) and permission.method.upper() == method.upper():
                if DEBUG_ENABLED:
                    print("---------------------------")
                    print(permission.name)
                    print(permission.url)
                    print(path)
                    print(permission.method)
                    print(method)
                    print("---------------------------")

                return True

        return False

    @staticmethod
    def user_is_authorized2(username: str, request: Request) -> bool:
        db: Session = SessionLocal()
        routes = request.app.router.routes

        name = ""

        # TODO: Check how this work.
        for route in routes:
            match, scope = route.matches(request)
            if match == Match.FULL:
                name = route.name

        user = db.query(User).where(User.username == username).first()

        db.close()

        if name in ADMIN_ROUTES and (user.admin or user.super_admin):
            return True
        elif name in SUPERADMIN_ROUTES and user.super_admin:
            return True
        elif name in ADMIN_ROUTES or name in SUPERADMIN_ROUTES:
            return False
        return True
