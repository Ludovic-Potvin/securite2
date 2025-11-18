import base64
import os
import hashlib


def hash_master_password(plain_password, salt=None) -> tuple[str, str]:
    if salt is None:
        salt: bytes = os.urandom(16)

    pwd_bytes = plain_password.encode("utf-8")
    digest = hashlib.sha256(pwd_bytes + salt).digest()

    password_b64 = base64.b64encode(digest).decode()
    salt_b64 = base64.b64encode(salt).decode()

    return password_b64, salt_b64


def encrypte_password(password: str, master_password: str) -> None:
    pass


def decrypte_password(password: str, master_password: str) -> None:
    pass
