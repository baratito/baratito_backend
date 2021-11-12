"""Added purchase overview_polyline column

Revision ID: 1125a340929e
Revises: 195f6cbef364
Create Date: 2021-11-12 06:45:47.256622

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1125a340929e"
down_revision = "195f6cbef364"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("purchase_list", sa.Column("overview_polyline", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("purchase_list", "overview_polyline")