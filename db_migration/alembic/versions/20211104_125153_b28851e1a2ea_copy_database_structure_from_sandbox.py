"""copy database structure from sandbox

Revision ID: b28851e1a2ea
Revises:
Create Date: 2021-11-04 12:51:53.151314

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b28851e1a2ea"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "drs_objects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("drs_id", sa.String(), nullable=False),
        sa.Column("path", sa.String(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("created_time", sa.DateTime(), nullable=False),
        sa.Column("checksum_md5", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("drs_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("drs_objects")
    # ### end Alembic commands ###
