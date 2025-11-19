import os
from pathlib import Path
from peewee import SqliteDatabase, Model
from playhouse.sqlcipher_ext import SqlCipherDatabase


DB_LOCATION: str = os.getenv(
    "DB_PATH", str(Path(__file__).resolve().parent.parent.parent / "db" / "database.db")
)
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "SuperSecretPassword123")

Path(DB_LOCATION).parent.mkdir(parents=True, exist_ok=True)

db: SqliteDatabase = SqlCipherDatabase(database=DB_LOCATION, passphrase=DB_PASSWORD)


class BaseModel(Model):
    class Meta:
        database: SqliteDatabase = db
