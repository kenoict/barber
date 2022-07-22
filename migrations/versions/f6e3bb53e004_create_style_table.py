"""Create style table

Revision ID: f6e3bb53e004
Revises: 31ee10aac357
Create Date: 2022-05-29 20:24:44.557220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6e3bb53e004'
down_revision = '31ee10aac357'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('style',
    sa.Column('id', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('barber_styles',
    sa.Column('barber_id', sa.String(length=100), nullable=False),
    sa.Column('style_id', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['barber_id'], ['barber.id'], ),
    sa.ForeignKeyConstraint(['style_id'], ['style.id'], ),
    sa.PrimaryKeyConstraint('barber_id', 'style_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('barber_styles')
    op.drop_table('style')
    # ### end Alembic commands ###
