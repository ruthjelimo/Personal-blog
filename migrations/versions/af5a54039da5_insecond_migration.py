"""Insecond  Migration

Revision ID: af5a54039da5
Revises: 8b38eacdd9e4
Create Date: 2022-03-14 11:13:24.985355

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af5a54039da5'
down_revision = '8b38eacdd9e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    op.add_column('blogs', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('blogs', sa.Column('title_blog', sa.String(length=255), nullable=True))
    op.add_column('blogs', sa.Column('description', sa.String(length=255), nullable=True))
    op.alter_column('blogs', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_blogs_description'), 'blogs', ['description'], unique=False)
    op.create_index(op.f('ix_blogs_title_blog'), 'blogs', ['title_blog'], unique=False)
    op.drop_constraint('blogs_user_id_fkey', 'blogs', type_='foreignkey')
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('blogs', 'blog_title')
    op.drop_column('blogs', 'posted_at')
    op.drop_column('blogs', 'blog_content')
    op.add_column('comments', sa.Column('date', sa.DateTime(), nullable=True))
    op.drop_constraint('comments_blog_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('comments', 'comment_date')
    op.add_column('users', sa.Column('firstname', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('lastname', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('date_joined', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_joined')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'lastname')
    op.drop_column('users', 'firstname')
    op.add_column('comments', sa.Column('comment_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key('comments_blog_id_fkey', 'comments', 'blogs', ['blog_id'], ['id'])
    op.drop_column('comments', 'date')
    op.add_column('blogs', sa.Column('blog_content', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('posted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('blog_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.create_foreign_key('blogs_user_id_fkey', 'blogs', 'users', ['user_id'], ['id'])
    op.drop_index(op.f('ix_blogs_title_blog'), table_name='blogs')
    op.drop_index(op.f('ix_blogs_description'), table_name='blogs')
    op.alter_column('blogs', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('blogs', 'description')
    op.drop_column('blogs', 'title_blog')
    op.drop_column('blogs', 'date')
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.drop_table('subscribers')
    # ### end Alembic commands ###