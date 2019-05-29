"""Added Term to Lesson

Revision ID: 326958e3bdc1
Revises: 587bc045e39b
Create Date: 2019-05-27 14:36:23.517113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '326958e3bdc1'
down_revision = '587bc045e39b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lesson', sa.Column('term', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lesson', 'term')
    # ### end Alembic commands ###
