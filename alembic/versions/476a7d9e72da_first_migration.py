"""first migration

Revision ID: 476a7d9e72da
Revises: 
Create Date: 2023-03-06 22:45:55.319460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '476a7d9e72da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_status', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('category', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('expiration_black_list', 'register_datetime',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('expiration_black_list', 'token',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
               nullable=False)
    op.alter_column('gender', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('message', 'register_datetime',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('message', 'header',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
               nullable=False)
    op.alter_column('message', 'body',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=4000),
               nullable=False)
    op.alter_column('permission', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('permission', 'url',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=1000),
               nullable=False)
    op.alter_column('permission', 'method',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=10),
               nullable=False)
    op.alter_column('person', 'surname',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('person', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('person', 'identification_number',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('person', 'birthdate',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('person', 'id_gender',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('person', 'id_department',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('person', 'address_street',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=250),
               nullable=False)
    op.alter_column('person', 'address_number',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('person', 'id_usual_institution',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('person', 'is_diabetic',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=False)
    op.alter_column('person', 'is_hypertensive',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=False)
    op.alter_column('person', 'is_chronic_respiratory_disease',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=False)
    op.alter_column('person', 'is_chronic_kidney_disease',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=False)
    op.alter_column('person', 'identification_number_master',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('person', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=True)
    op.alter_column('person', 'id_admin_status',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               existing_server_default=sa.text('1'))
    op.alter_column('person', 'phone_number',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('person', 'department',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=200),
               nullable=False)
    op.alter_column('person', 'locality',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=200),
               nullable=False)
    op.alter_column('person', 'email',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=200),
               nullable=False)
    op.alter_column('person', 'identification_front_image',
               existing_type=mysql.LONGTEXT(collation='latin1_spanish_ci'),
               nullable=True)
    op.alter_column('person', 'identification_back_image',
               existing_type=mysql.LONGTEXT(collation='latin1_spanish_ci'),
               nullable=True)
    op.alter_column('person', 'identification_front_image_file_type',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=45),
               nullable=True)
    op.alter_column('person', 'identification_back_image_file_type',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=45),
               nullable=True)
    op.alter_column('person_message', 'id_person',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('person_message', 'id_message',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('person_message', 'read_datetime',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=45),
               nullable=True)
    op.alter_column('person_status', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('role', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('role_permission', 'id_permission',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('role_permission', 'id_role',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
               nullable=False,
               existing_server_default=sa.text("''"))
    op.alter_column('user', 'is_admin',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('user_category', 'id_user',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('user_category', 'id_category',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('user_role', 'id_role',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('user_role', 'id_user',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_role', 'id_user',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('user_role', 'id_role',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('user_category', 'id_category',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('user_category', 'id_user',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('user', 'is_admin',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
               nullable=True,
               existing_server_default=sa.text("''"))
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('role_permission', 'id_role',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('role_permission', 'id_permission',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('role', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('person_status', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('person_message', 'read_datetime',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=45),
               nullable=True)
    op.alter_column('person_message', 'id_message',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('person_message', 'id_person',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('person', 'identification_back_image_file_type',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=45),
               nullable=True)
    op.alter_column('person', 'identification_front_image_file_type',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=45),
               nullable=True)
    op.alter_column('person', 'identification_back_image',
               existing_type=mysql.LONGTEXT(collation='latin1_spanish_ci'),
               nullable=True)
    op.alter_column('person', 'identification_front_image',
               existing_type=mysql.LONGTEXT(collation='latin1_spanish_ci'),
               nullable=True)
    op.alter_column('person', 'email',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=200),
               nullable=True)
    op.alter_column('person', 'locality',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=200),
               nullable=True)
    op.alter_column('person', 'department',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=200),
               nullable=True)
    op.alter_column('person', 'phone_number',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('person', 'id_admin_status',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               existing_server_default=sa.text('1'))
    op.alter_column('person', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=True)
    op.alter_column('person', 'identification_number_master',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('person', 'is_chronic_kidney_disease',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=True)
    op.alter_column('person', 'is_chronic_respiratory_disease',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=True)
    op.alter_column('person', 'is_hypertensive',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=True)
    op.alter_column('person', 'is_diabetic',
               existing_type=mysql.TINYINT(display_width=4),
               nullable=True)
    op.alter_column('person', 'id_usual_institution',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('person', 'address_number',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True
               )
    op.alter_column('person', 'address_street',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=250),
               nullable=True)
    op.alter_column('person', 'id_department',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('person', 'id_gender',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('person', 'birthdate',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('person', 'identification_number',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('person', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('person', 'surname',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('permission', 'method',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=10),
               nullable=True)
    op.alter_column('permission', 'url',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=1000),
               nullable=True)
    op.alter_column('permission', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('message', 'body',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=4000),
               nullable=True)
    op.alter_column('message', 'header',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
               nullable=True)
    op.alter_column('message', 'register_datetime',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('gender', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('expiration_black_list', 'token',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=500),
               nullable=True)
    op.alter_column('expiration_black_list', 'register_datetime',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('category', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    op.alter_column('admin_status', 'name',
               existing_type=mysql.VARCHAR(collation='latin1_spanish_ci', length=100),
               nullable=True)
    # ### end Alembic commands ###
