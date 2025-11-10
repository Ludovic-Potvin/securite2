import os
from pathlib import Path
from peewee import SqliteDatabase, Model


DB_LOCATION: str = os.getenv(
    "DB_PATH", str(Path(__file__).resolve().parent.parent.parent / "db" / "database.db")
)

Path(DB_LOCATION).parent.mkdir(parents=True, exist_ok=True)

db: SqliteDatabase = SqliteDatabase(database=DB_LOCATION)


class BaseModel(Model):
    class Meta:
        database: SqliteDatabase = db
