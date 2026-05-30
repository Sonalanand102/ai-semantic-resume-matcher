"""add experience and employment fields to jobs

Revision ID: c9f2e1a47b2d
Revises: 437c69bf1186
Create Date: 2026-05-28 01:45:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c9f2e1a47b2d"
down_revision: Union[str, Sequence[str], None] = "437c69bf1186"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("jobs", sa.Column("experience_level", sa.Text(), nullable=True))
    op.add_column("jobs", sa.Column("employment_type", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("jobs", "employment_type")
    op.drop_column("jobs", "experience_level")
