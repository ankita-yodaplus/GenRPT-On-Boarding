"""Added adress to company

Revision ID: 9c826a92415b
Revises: 91dbcfa6eb78
Create Date: 2025-05-08 14:40:49.772513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c826a92415b'
down_revision: Union[str, None] = '91dbcfa6eb78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('address', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'address')
    # ### end Alembic commands ###
