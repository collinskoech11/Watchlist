"""Initial Migration

Revision ID: 421cd18fadef
Revises: 
Create Date: 2018-04-11 10:36:17.367050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '421cd18fadef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
