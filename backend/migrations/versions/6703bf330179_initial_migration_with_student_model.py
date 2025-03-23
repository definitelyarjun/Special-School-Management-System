"""Initial migration with Student model

Revision ID: 6703bf330179
Revises: e291d2caff88
Create Date: 2025-03-23 21:25:56.502217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6703bf330179'
down_revision: Union[str, None] = 'e291d2caff88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('religion', sa.String(), nullable=True),
    sa.Column('caste', sa.String(), nullable=True),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.Column('roll_no', sa.String(), nullable=True),
    sa.Column('birth_place', sa.String(), nullable=True),
    sa.Column('house_name', sa.String(), nullable=True),
    sa.Column('street_name', sa.String(), nullable=True),
    sa.Column('post_office', sa.String(), nullable=True),
    sa.Column('pin_code', sa.String(), nullable=True),
    sa.Column('revenue_district', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('father_name', sa.String(), nullable=True),
    sa.Column('father_education', sa.String(), nullable=True),
    sa.Column('father_occupation', sa.String(), nullable=True),
    sa.Column('mother_name', sa.String(), nullable=True),
    sa.Column('mother_education', sa.String(), nullable=True),
    sa.Column('mother_occupation', sa.String(), nullable=True),
    sa.Column('guardian_name', sa.String(), nullable=True),
    sa.Column('guardian_relationship', sa.String(), nullable=True),
    sa.Column('guardian_contact', sa.String(), nullable=True),
    sa.Column('academic_year', sa.String(), nullable=True),
    sa.Column('admission_number', sa.String(), nullable=True),
    sa.Column('admission_date', sa.Date(), nullable=True),
    sa.Column('class_teacher', sa.String(), nullable=True),
    sa.Column('bank_name', sa.String(), nullable=True),
    sa.Column('account_number', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=True),
    sa.Column('ifsc_code', sa.String(), nullable=True),
    sa.Column('disability_type', sa.String(), nullable=True),
    sa.Column('disability_percentage', sa.Float(), nullable=True),
    sa.Column('medical_conditions', sa.Text(), nullable=True),
    sa.Column('allergies', sa.Text(), nullable=True),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_id'), 'students', ['id'], unique=False)
    op.create_index(op.f('ix_students_name'), 'students', ['name'], unique=False)
    op.create_index(op.f('ix_students_student_id'), 'students', ['student_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_student_id'), table_name='students')
    op.drop_index(op.f('ix_students_name'), table_name='students')
    op.drop_index(op.f('ix_students_id'), table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###
