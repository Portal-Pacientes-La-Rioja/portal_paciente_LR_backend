"""Create Studies tables

Revision ID: df75caff7046
Revises: 23d1c62160fb
Create Date: 2023-08-06 11:40:31.287167

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'df75caff7046'
down_revision = '23d1c62160fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('study_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('studies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_person', sa.BIGINT(), nullable=False),
    sa.Column('id_study_type', sa.Integer(), nullable=False),
    sa.Column('study_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.Column('upload_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_study_type'], ['study_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    op.create_foreign_key(None,
                          "studies", "person",
                          ["id_person"], ["id"])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('studies')
    op.drop_table('study_type')
    # ### end Alembic commands ###
