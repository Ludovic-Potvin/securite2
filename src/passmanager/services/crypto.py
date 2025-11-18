import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class CryptoService:
    @staticmethod
    def hash_master_password(
        username: str, password: str, salt: bytes | None = None
    ) -> tuple[str, str]:
        if salt is None:
            salt = os.urandom(16)
        digest: hashes.Hash = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password.encode("utf-8"))

        # 4. Calculer le hachage
        hash_bytes = digest.finalize()

        # 5. Encoder en base64
        password_base64 = base64.b64encode(hash_bytes).decode("utf-8")
        salt_base64 = base64.b64encode(salt).decode("utf-8")

        return password_base64, salt_base64

    @staticmethod
    def get_master_salt(username: str) -> None:
        pass

    @staticmethod
    def encrypte_password(password: str, master_password: str) -> None:
        pass

    @staticmethod
    def decrypte_password(password: str, master_password: str) -> None:
        pass
