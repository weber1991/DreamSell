"""empty message

Revision ID: bf42c9779d0a
Revises: 832b95898f8f
Create Date: 2019-11-09 21:07:46.147507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf42c9779d0a'
down_revision = '832b95898f8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders_detail', sa.Column('note1', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders_detail', 'note1')
    # ### end Alembic commands ###