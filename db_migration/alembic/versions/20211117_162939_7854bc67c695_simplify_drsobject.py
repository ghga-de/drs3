"""simplify drsobject

Revision ID: 7854bc67c695
Revises: b28851e1a2ea
Create Date: 2021-11-17 16:29:39.753168

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "7854bc67c695"
down_revision = "b28851e1a2ea"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("drs_objects", sa.Column("external_id", sa.String(), nullable=False))
    op.add_column("drs_objects", sa.Column("md5_checksum", sa.String(), nullable=False))
    op.add_column(
        "drs_objects", sa.Column("registration_date", sa.DateTime(), nullable=False)
    )
    op.drop_constraint("drs_objects_drs_id_key", "drs_objects", type_="unique")
    op.create_unique_constraint(None, "drs_objects", ["external_id"])
    op.drop_column("drs_objects", "path")
    op.drop_column("drs_objects", "created_time")
    op.drop_column("drs_objects", "checksum_md5")
    op.drop_column("drs_objects", "drs_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "drs_objects",
        sa.Column("drs_id", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "drs_objects",
        sa.Column("checksum_md5", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "drs_objects",
        sa.Column(
            "created_time", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "drs_objects",
        sa.Column("path", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "drs_objects", type_="unique")
    op.create_unique_constraint("drs_objects_drs_id_key", "drs_objects", ["drs_id"])
    op.drop_column("drs_objects", "registration_date")
    op.drop_column("drs_objects", "md5_checksum")
    op.drop_column("drs_objects", "external_id")
    # ### end Alembic commands ###
