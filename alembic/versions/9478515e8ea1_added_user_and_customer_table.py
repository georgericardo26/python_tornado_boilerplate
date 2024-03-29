"""Added user and customer table

Revision ID: 9478515e8ea1
Revises: 
Create Date: 2022-04-21 22:32:43.352216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9478515e8ea1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_created_at'), 'user', ['created_at'], unique=False)
    op.create_table('customer',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('account_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    op.drop_index(op.f('ix_user_created_at'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
