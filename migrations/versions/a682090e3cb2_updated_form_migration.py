"""updated form   Migration

Revision ID: a682090e3cb2
Revises: af5a54039da5
Create Date: 2022-03-14 11:18:47.180119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a682090e3cb2'
down_revision = 'af5a54039da5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'firstname')
    op.drop_column('users', 'lastname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lastname', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('firstname', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
