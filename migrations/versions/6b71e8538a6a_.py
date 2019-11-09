"""empty message

Revision ID: 6b71e8538a6a
Revises: bf42c9779d0a
Create Date: 2019-11-09 21:13:19.397130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b71e8538a6a'
down_revision = 'bf42c9779d0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders_detail', sa.Column('note2', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders_detail', 'note2')
    # ### end Alembic commands ###