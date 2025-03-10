"""empty message

Revision ID: ae365aadb0dd
Revises: f57873e1c499
Create Date: 2025-03-09 20:44:03.379240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'ae365aadb0dd'
down_revision: Union[str, None] = 'f57873e1c499'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contactentrymodel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contactentrymodel', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
