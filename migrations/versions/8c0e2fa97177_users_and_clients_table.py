"""Users and Clients table

Revision ID: 8c0e2fa97177
Revises: 
Create Date: 2020-11-28 18:18:42.686751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c0e2fa97177'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('f_name', sa.String(length=32), nullable=True),
    sa.Column('l_name', sa.String(length=32), nullable=True),
    sa.Column('allergies', sa.Boolean(), nullable=True),
    sa.Column('room', sa.String(length=32), nullable=True),
    sa.Column('medication', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_clients_f_name'), 'clients', ['f_name'], unique=False)
    op.create_index(op.f('ix_clients_l_name'), 'clients', ['l_name'], unique=False)
    op.create_index(op.f('ix_clients_medication'), 'clients', ['medication'], unique=False)
    op.create_index(op.f('ix_clients_room'), 'clients', ['room'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('f_name', sa.String(length=64), nullable=True),
    sa.Column('l_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_f_name'), 'users', ['f_name'], unique=False)
    op.create_index(op.f('ix_users_l_name'), 'users', ['l_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_l_name'), table_name='users')
    op.drop_index(op.f('ix_users_f_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_clients_room'), table_name='clients')
    op.drop_index(op.f('ix_clients_medication'), table_name='clients')
    op.drop_index(op.f('ix_clients_l_name'), table_name='clients')
    op.drop_index(op.f('ix_clients_f_name'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###
