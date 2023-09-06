"""tikker_id

Revision ID: 6b7e9b27249c
Revises: 98bc3f2d9951
Create Date: 2023-09-06 22:22:11.427842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b7e9b27249c'
down_revision: Union[str, None] = '98bc3f2d9951'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('currency', sa.Column('tikker_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'currency', ['tikker_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'currency', type_='unique')
    op.drop_column('currency', 'tikker_id')
    # ### end Alembic commands ###