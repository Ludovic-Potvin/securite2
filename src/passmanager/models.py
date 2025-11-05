from passmanager.db import get_db_connection


class User:
    @staticmethod
    def get(username: str) -> str:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM user WHERE username = ?", (username,))
        row = cursor.fetchone()

        return row[0] if row else ""

    @staticmethod
    def create(username: str, password: str) -> str:
        return "TODO"

    @staticmethod
    def delete(username: str) -> str:
        return "TODO"

    @staticmethod
    def update(username: str, password: str) -> str:
        return "TODO"


class Password:
    @staticmethod
    def get(label: str) -> str:
        return "TODO"

    @staticmethod
    def create(username: str, label: str, password: str) -> str:
        return "TODO"

    @staticmethod
    def delete(label: str) -> str:
        return "TODO"

    @staticmethod
    def update(label: str, password: str) -> str:
        return "TODO"
