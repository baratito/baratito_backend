"""Change field name

Revision ID: 4b5fef299b0b
Revises: a1ea0f7524ba
Create Date: 2021-11-21 15:06:01.180003

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4b5fef299b0b"
down_revision = "a1ea0f7524ba"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("purchase_list_item", sa.Column("is_bought", sa.Boolean(), nullable=True))
    op.drop_column("purchase_list_item", "is_buyed")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "purchase_list_item",
        sa.Column("is_buyed", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.drop_column("purchase_list_item", "is_bought")

    # ### end Alembic commands ###
