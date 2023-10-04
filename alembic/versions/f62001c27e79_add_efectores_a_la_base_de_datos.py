"""Add efectores a la base de datos

Revision ID: f62001c27e79
Revises: 1382cc7242e0
Create Date: 2023-04-01 14:57:52.230592

"""
import csv

from alembic import op
from sqlalchemy import orm

session = orm.Session(bind=op)

from pathlib import Path
from app.models.institutions import Institutions
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = 'f62001c27e79'
down_revision = '1382cc7242e0'
branch_labels = None
depends_on = None

LISTADO_EFECTORES_FILE = Path(__file__).parent.parent.parent / "database/Efectores_LR.csv"


def upgrade():
    session = orm.Session(bind=op.get_bind())
    op.alter_column('institutions', 'domicilio',
                    existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
                    type_=mysql.VARCHAR(length=500),
                    existing_nullable=False)

    # migracion efectores
    with open(LISTADO_EFECTORES_FILE) as f:
        csv_file = csv.DictReader(f)

        for line in csv_file:
            institutions = Institutions(
                codigo=line["codigo"],
                name=line["name"],
                domicilio=line["domicilio"],
                tipologia=line["tipo"],
                categoria_tipologia=line["categoria"],
                dependencia=line["dependencia"],
                departamento=line["departamento"],
                localidad=line["localidad"],
                ciudad=line["ciudad"]
            )

            session.add(institutions)

        session.commit()


def downgrade():
    op.alter_column('institutions', 'domicilio',
                    existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
                    type_=mysql.VARCHAR(length=100),
                    existing_nullable=False)
    pass
