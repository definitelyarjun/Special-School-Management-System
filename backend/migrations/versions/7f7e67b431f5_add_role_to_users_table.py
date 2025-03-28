"""Add role to users table

Revision ID: 7f7e67b431f5
Revises: 322962e49476
Create Date: 2025-03-27 18:50:22.020241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f7e67b431f5'
down_revision: Union[str, None] = '322962e49476'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_students_student_id', table_name='students')
    op.create_index(op.f('ix_students_student_id'), 'students', ['student_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_student_id'), table_name='students')
    op.create_index('ix_students_student_id', 'students', ['student_id'], unique=False)
    # ### end Alembic commands ###
