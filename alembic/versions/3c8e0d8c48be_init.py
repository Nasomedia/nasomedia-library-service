"""init

Revision ID: 3c8e0d8c48be
Revises: 
Create Date: 2021-12-05 19:53:42.217267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c8e0d8c48be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latest_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_history_id'), 'history', ['id'], unique=False)
    op.create_table('liked',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('series_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_liked_id'), 'liked', ['id'], unique=False)
    op.create_table('purchased',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_purchased_id'), 'purchased', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_purchased_id'), table_name='purchased')
    op.drop_table('purchased')
    op.drop_index(op.f('ix_liked_id'), table_name='liked')
    op.drop_table('liked')
    op.drop_index(op.f('ix_history_id'), table_name='history')
    op.drop_table('history')
    # ### end Alembic commands ###