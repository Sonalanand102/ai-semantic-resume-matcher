"""add search text

Revision ID: c0946d0cbb96
Revises: c9f2e1a47b2d
Create Date: 2026-05-28 02:31:39.110307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0946d0cbb96'
down_revision: Union[str, Sequence[str], None] = 'c9f2e1a47b2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("jobs", sa.Column("search_text", sa.Text(), nullable=True))
    op.execute(
        """
        UPDATE jobs
        SET search_text = CONCAT_WS(' ', company_name, job_title, location, job_description)
        WHERE search_text IS NULL
        """
    )
    op.alter_column("jobs", "search_text", nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("jobs", "search_text")
