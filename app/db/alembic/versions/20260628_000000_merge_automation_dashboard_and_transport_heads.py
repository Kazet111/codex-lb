"""merge automation/dashboard and upstream transport heads

Revision ID: 20260628_000000_merge_automation_dashboard_and_transport_heads
Revises:
- 20260615_000000_merge_automations_and_dashboard_guest_heads
- 20260626_010000_add_request_logs_upstream_transport
Create Date: 2026-06-28 00:00:00.000000
"""

from __future__ import annotations

revision = "20260628_000000_merge_automation_dashboard_and_transport_heads"
down_revision = (
    "20260615_000000_merge_automations_and_dashboard_guest_heads",
    "20260626_010000_add_request_logs_upstream_transport",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
