def upgrade() -> None:
    op.create_table(
        'rooms',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('hotel_id', sa.Integer(), sa.ForeignKey('hotels.id'), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('rooms')