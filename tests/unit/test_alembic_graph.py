from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest
from alembic import command
from alembic.script import ScriptDirectory

from app.db.migrate import _build_alembic_config

_HEAD = "20260630_000000_merge_automations_and_dashboard_index_heads"
_FORMER_HEADS = (
    "20260628_000000_merge_automation_dashboard_and_transport_heads",
    "20260629_000000_add_dashboard_query_hot_path_indexes",
)


def test_alembic_graph_has_single_merged_head() -> None:
    config = _build_alembic_config("sqlite:///unused.db")
    script_directory = ScriptDirectory.from_config(config)
    merge_revision = script_directory.get_revision(_HEAD)

    assert script_directory.get_heads() == [_HEAD]
    assert merge_revision is not None
    assert merge_revision.down_revision == _FORMER_HEADS


@pytest.mark.parametrize("starting_revision", (None, *_FORMER_HEADS))
def test_upgrade_reaches_merged_head(tmp_path: Path, starting_revision: str | None) -> None:
    db_path = tmp_path / "migration.db"
    config = _build_alembic_config(f"sqlite:///{db_path}")

    if starting_revision is not None:
        command.upgrade(config, starting_revision)
    command.upgrade(config, "head")

    with sqlite3.connect(db_path) as connection:
        rows = connection.execute("SELECT version_num FROM alembic_version").fetchall()
    assert rows == [(_HEAD,)]
