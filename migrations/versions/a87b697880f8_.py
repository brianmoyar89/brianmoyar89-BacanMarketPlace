"""empty message

Revision ID: a87b697880f8
Revises: 
Create Date: 2023-08-22 23:07:19.513048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a87b697880f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('user_name', sa.String(length=120), nullable=False),
    sa.Column('cellphone', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cellphone'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###