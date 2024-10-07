from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7944454d1ded'
down_revision = 'cfc5cae7d7a3'
branch_labels = None
depends_on = None

def upgrade():
    # Rename 'address' column to 'location'
    op.rename_column('departments', 'address', 'location')

def downgrade():
    # Rename 'location' column back to 'address'
    op.rename_column('departments', 'location', 'address')
