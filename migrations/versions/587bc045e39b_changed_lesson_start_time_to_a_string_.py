"""Changed lesson start time to a string data field

Revision ID: 587bc045e39b
Revises: 9df3dcc11469
Create Date: 2019-05-27 12:54:47.767899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '587bc045e39b'
down_revision = '9df3dcc11469'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lesson', sa.Column('lesson_time', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lesson', 'lesson_time')
    # ### end Alembic commands ###
