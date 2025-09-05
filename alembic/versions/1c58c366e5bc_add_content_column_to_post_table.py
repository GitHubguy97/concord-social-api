"""add content column to post table

Revision ID: 1c58c366e5bc
Revises: 105694c084a2
Create Date: 2025-09-04 21:41:05.165007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c58c366e5bc'
down_revision: Union[str, Sequence[str], None] = '105694c084a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
