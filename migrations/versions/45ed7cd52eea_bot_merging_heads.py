"""[bot]merging heads

Revision ID: 45ed7cd52eea
Revises: 0ba9654475a5, eb62cdc96051
Create Date: 2024-11-14 16:58:54.680149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45ed7cd52eea'
down_revision = ('0ba9654475a5', 'eb62cdc96051')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
