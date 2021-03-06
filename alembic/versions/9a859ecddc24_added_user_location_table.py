"""Added User location table

Revision ID: 9a859ecddc24
Revises: 091e41f5f089
Create Date: 2021-10-11 20:50:13.964929

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9a859ecddc24"
down_revision = "091e41f5f089"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_location",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.Column("enable", sa.Boolean(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("country", sa.String(), nullable=True),
        sa.Column("user_id", sa.BIGINT(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_location_id"), "user_location", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("idx_establishment_location", "establishment", ["location"], unique=False)
    op.drop_index(op.f("ix_user_location_id"), table_name="user_location")
    op.drop_table("user_location")
    # ### end Alembic commands ###
