"""empty message

Revision ID: 1936a485d4e3
Revises: 58c33ab276b1
Create Date: 2024-10-01 17:39:40.477894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1936a485d4e3'
down_revision = '58c33ab276b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
