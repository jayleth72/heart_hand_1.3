"""added leson start date to lesson and deleted lesson_recurring data

Revision ID: 7476fdb0baac
Revises: 6ae90fceb335
Create Date: 2019-02-05 21:45:19.972925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7476fdb0baac'
down_revision = '6ae90fceb335'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lesson', sa.Column('lesson_start_date', sa.DateTime(), nullable=False))
    op.drop_column('lesson', 'lesson_recurring')
    op.drop_column('lesson', 'lesson_recurring_period')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lesson', sa.Column('lesson_recurring_period', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('lesson', sa.Column('lesson_recurring', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('lesson', 'lesson_start_date')
    # ### end Alembic commands ###