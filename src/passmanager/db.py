import sqlite3
import os
from pathlib import Path

_conn: sqlite3.Connection | None = None


def init_db() -> None:
    get_db_connection()
    create_tables()


def get_db_connection() -> sqlite3.Connection:
    global _conn

    if _conn is None:
        db_path = os.getenv("DB_PATH", "../db/database.db")
        absolute_path = Path(__file__).resolve().parent.joinpath(db_path).resolve()
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        _conn = sqlite3.connect(str(absolute_path))

    return _conn


def create_tables() -> None:
    conn: sqlite3.Connection = get_db_connection()
    cursor: sqlite3.Cursor = conn.cursor()

    # Create users table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """
    )

    # Create password table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS password (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        label TEXT NOT NULL,
        password TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES user(id)
    )
    """
    )

    conn.commit()
