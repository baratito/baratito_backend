"""Added photo to product

Revision ID: 091e41f5f089
Revises: 0bba8953a559
Create Date: 2021-10-11 00:04:11.067066

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "091e41f5f089"
down_revision = "0bba8953a559"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("product", sa.Column("photo", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("product", "photo")
