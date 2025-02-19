"""Edit auth type and config class column

Revision ID: d15993654ea8
Revises: 153d267e9152
Create Date: 2024-12-29 17:01:45.825790

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'd15993654ea8'
down_revision = '153d267e9152'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('integration_credential', sa.Column('auth_type', sa.String(), nullable=False))
    op.alter_column('integration_credential', 'auth_config_class',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('integration_credential', 'auth_credential_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('integration_credential', sa.Column('auth_credential_type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('integration_credential', 'auth_config_class',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('integration_credential', 'auth_type')
    # ### end Alembic commands ###
