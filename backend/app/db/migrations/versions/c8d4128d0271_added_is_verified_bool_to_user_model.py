"""Added is_verified bool to User Model

Revision ID: c8d4128d0271
Revises: fdf8821871d7
Create Date: 2023-06-03 01:43:29.263372

"""
from alembic import op
import sqlalchemy as sa


revision = 'c8d4128d0271'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=False, default=False))


def downgrade() -> None:
    op.drop_column('users', 'is_verified')

