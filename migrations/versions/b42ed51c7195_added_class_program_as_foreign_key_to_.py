"""Added class program as foreign key to payments, also made lesson id nullable is True on same table

Revision ID: b42ed51c7195
Revises: 61fc851d5963
Create Date: 2019-05-27 09:48:47.941332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b42ed51c7195'
down_revision = '61fc851d5963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payments', sa.Column('class_program_id', sa.Integer(), nullable=True))
    op.alter_column('payments', 'lesson_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'payments', 'class_program', ['class_program_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payments', type_='foreignkey')
    op.alter_column('payments', 'lesson_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('payments', 'class_program_id')
    # ### end Alembic commands ###
