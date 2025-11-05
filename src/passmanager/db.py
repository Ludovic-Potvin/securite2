import sqlite3
import os
from pathlib import Path


def init_db() -> None:
    db_path: str = os.getenv("DB_PATH", "../db/database.db")
    path: Path = Path(db_path)

    absolute_path = Path(__file__).resolve().parent.joinpath(db_path).resolve()

    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(absolute_path))
    conn.close()
