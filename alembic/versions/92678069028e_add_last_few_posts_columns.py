"""add last few posts columns

Revision ID: 92678069028e
Revises: 709a446e7f46
Create Date: 2025-09-04 22:30:56.669703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92678069028e'
down_revision: Union[str, Sequence[str], None] = '709a446e7f46'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default = sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts',"published")
    op.drop_column('posts', 'created_at')
    pass
