"""Add product category constraint

Revision ID: 0bba8953a559
Revises: d94fc87b96fa
Create Date: 2021-10-09 20:59:34.864581

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0bba8953a559"
down_revision = "d94fc87b96fa"
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(None, "category_product", ["product_id", "category_id"])


def downgrade():
    op.drop_constraint(None, "category_product", type_="unique")
