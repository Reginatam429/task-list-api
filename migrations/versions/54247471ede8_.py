"""empty message

Revision ID: 54247471ede8
Revises: 34571d40858b
Create Date: 2021-06-14 22:02:53.429433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54247471ede8'
down_revision = '34571d40858b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
