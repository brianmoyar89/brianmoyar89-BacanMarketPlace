"""empty message

Revision ID: 2f781ea252e7
Revises: ede4fabe27b4
Create Date: 2023-08-31 02:27:41.397056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f781ea252e7'
down_revision = 'ede4fabe27b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('interested_product_one', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('interested_product_two', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('interested_product_three', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('product_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_type', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('interested_product_three')
        batch_op.drop_column('interested_product_two')
        batch_op.drop_column('interested_product_one')
        batch_op.drop_column('image')

    # ### end Alembic commands ###
