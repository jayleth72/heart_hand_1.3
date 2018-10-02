"""third migration

Revision ID: e1331e9c3189
Revises: b77c734e6a29
Create Date: 2018-09-07 21:31:44.042165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1331e9c3189'
down_revision = 'b77c734e6a29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class_program',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('program_name', sa.String(length=80), nullable=True),
    sa.Column('program_cost', sa.Float(), nullable=True),
    sa.Column('program_discount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('lesson', sa.Column('lesson_recurring', sa.Boolean(), nullable=True))
    op.add_column('lesson', sa.Column('lesson_recurring_period', sa.String(length=80), nullable=True))
    op.add_column('payments', sa.Column('payment_description', sa.String(length=255), nullable=True))
    op.drop_column('payments', 'cost_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payments', sa.Column('cost_description', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('payments', 'payment_description')
    op.drop_column('lesson', 'lesson_recurring_period')
    op.drop_column('lesson', 'lesson_recurring')
    op.drop_table('class_program')
    # ### end Alembic commands ###