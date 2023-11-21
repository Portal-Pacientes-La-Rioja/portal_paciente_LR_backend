"""Add phone number to institution model

Revision ID: c974b9d0bd83
Revises: f62001c27e79
Create Date: 2023-05-05 22:38:55.912230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c974b9d0bd83'
down_revision = 'f62001c27e79'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "institutions",
        sa.Column("telefono", sa.Integer, nullable=True, default_server="0")
    )
    pass


def downgrade():
    op.drop_column("institutions", "telefono")
    pass
