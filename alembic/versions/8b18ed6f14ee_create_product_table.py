"""Create product table

Revision ID: 8b18ed6f14ee
Revises: 
Create Date: 2021-08-10 06:39:16.511151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b18ed6f14ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('presentation', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('max_price', sa.Float(), nullable=True),
    sa.Column('min_price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###