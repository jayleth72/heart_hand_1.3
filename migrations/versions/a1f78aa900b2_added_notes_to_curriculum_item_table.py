"""added notes to Curriculum_item table

Revision ID: a1f78aa900b2
Revises: 9506f045ddd2
Create Date: 2019-05-22 18:56:09.454139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f78aa900b2'
down_revision = '9506f045ddd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curriculum_item', sa.Column('notes', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('curriculum_item', 'notes')
    # ### end Alembic commands ###
