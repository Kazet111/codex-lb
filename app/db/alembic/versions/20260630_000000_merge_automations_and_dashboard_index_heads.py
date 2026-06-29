"""merge automations and dashboard index heads

Revision ID: 20260630_000000_merge_automations_and_dashboard_index_heads
Revises:
- 20260628_000000_merge_automation_dashboard_and_transport_heads
- 20260629_000000_add_dashboard_query_hot_path_indexes
Create Date: 2026-06-30 00:00:00.000000
"""

from __future__ import annotations

revision = "20260630_000000_merge_automations_and_dashboard_index_heads"
down_revision = (
    "20260628_000000_merge_automation_dashboard_and_transport_heads",
    "20260629_000000_add_dashboard_query_hot_path_indexes",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
