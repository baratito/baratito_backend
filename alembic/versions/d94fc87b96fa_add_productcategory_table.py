"""Add productcategory table

Revision ID: d94fc87b96fa
Revises: 628a054dfe97
Create Date: 2021-09-21 23:01:56.425513

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d94fc87b96fa"
down_revision = "628a054dfe97"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category_product",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("product_id", sa.BIGINT(), nullable=True),
        sa.Column("category_id", sa.BIGINT(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_category_product_category_id"), "category_product", ["category_id"], unique=False
    )
    op.create_index(op.f("ix_category_product_id"), "category_product", ["id"], unique=False)
    op.create_index(
        op.f("ix_category_product_product_id"), "category_product", ["product_id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("idx_establishment_location", "establishment", ["location"], unique=False)
    op.create_table(
        "spatial_ref_sys",
        sa.Column("srid", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("auth_name", sa.VARCHAR(length=256), autoincrement=False, nullable=True),
        sa.Column("auth_srid", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("srtext", sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
        sa.Column("proj4text", sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
        sa.CheckConstraint("(srid > 0) AND (srid <= 998999)", name="spatial_ref_sys_srid_check"),
        sa.PrimaryKeyConstraint("srid", name="spatial_ref_sys_pkey"),
    )
    op.drop_index(op.f("ix_category_product_product_id"), table_name="category_product")
    op.drop_index(op.f("ix_category_product_id"), table_name="category_product")
    op.drop_index(op.f("ix_category_product_category_id"), table_name="category_product")
    op.drop_table("category_product")
    # ### end Alembic commands ###
