"""added curriculum fields

Revision ID: 9506f045ddd2
Revises: 7476fdb0baac
Create Date: 2019-05-20 16:54:13.080780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9506f045ddd2'
down_revision = '7476fdb0baac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(length=80), nullable=True),
    sa.Column('subject_description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('curriculum_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('year_level', sa.Integer(), nullable=True),
    sa.Column('term', sa.Integer(), nullable=True),
    sa.Column('topic', sa.String(length=80), nullable=True),
    sa.Column('learnt_skill', sa.String(length=80), nullable=True),
    sa.Column('concepts', sa.String(length=80), nullable=True),
    sa.Column('activity', sa.String(length=80), nullable=True),
    sa.Column('resources', sa.String(length=80), nullable=True),
    sa.Column('sample_to_collect', sa.String(length=80), nullable=True),
    sa.Column('information_recorded', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curriculum_item')
    op.drop_table('subjects')
    # ### end Alembic commands ###
