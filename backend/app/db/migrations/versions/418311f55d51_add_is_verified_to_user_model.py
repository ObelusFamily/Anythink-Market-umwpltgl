"""Add is_verified to User model

Revision ID: 418311f55d51
Revises: fdf8821871d7
Create Date: 2023-06-04 02:59:20.395761

"""
from alembic import op
import sqlalchemy as sa


revision = '418311f55d51'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # add new column set to True to alter existing records
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=True, default=False))
    # # alter exiting records
    # op.execute("UPDATE users SET is_verified = false")
    # # set column to not nullable
    # op.alter_column('users', 'is_verified', nullable=False, default=None)


def downgrade() -> None:
    op.drop_column('users', 'is_verified')

