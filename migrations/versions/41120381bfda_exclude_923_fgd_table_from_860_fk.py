"""Exclude 923 FGD table from 860 FK

Revision ID: 41120381bfda
Revises: b8ae440a2d32
Create Date: 2024-03-20 15:02:11.634526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41120381bfda'
down_revision = 'b8ae440a2d32'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('_core_eia923__fgd_operation_maintenance', schema=None) as batch_op:
        batch_op.drop_constraint('fk__core_eia923__fgd_operation_maintenance_plant_id_eia_core_eia860__scd_plants', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk__core_eia923__fgd_operation_maintenance_plant_id_eia_core_eia__entity_plants'), 'core_eia__entity_plants', ['plant_id_eia'], ['plant_id_eia'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('_core_eia923__fgd_operation_maintenance', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk__core_eia923__fgd_operation_maintenance_plant_id_eia_core_eia__entity_plants'), type_='foreignkey')
        batch_op.create_foreign_key('fk__core_eia923__fgd_operation_maintenance_plant_id_eia_core_eia860__scd_plants', 'core_eia860__scd_plants', ['plant_id_eia', 'report_date'], ['plant_id_eia', 'report_date'])

    # ### end Alembic commands ###
