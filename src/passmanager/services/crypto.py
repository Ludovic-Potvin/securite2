import base64
import os
import hashlib

from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def hash_master_password(plain_password, salt=None) -> tuple[str, str]:
    if salt is None:
        salt: bytes = os.urandom(16)

    pwd_bytes = plain_password.encode("utf-8")
    digest = hashlib.sha256(pwd_bytes + salt).digest()

    password_b64 = base64.b64encode(digest).decode()
    salt_b64 = base64.b64encode(salt).decode()

    return password_b64, salt_b64


def encrypte_password(password: str, master_password: str) -> tuple[str, str, str]:
    """
    Return: Password, salt and iv.
    """
    salt: bytes = os.urandom(16)
    aes_key = derive_aes_key(master_password, salt)
    iv = os.urandom(16)

    # Add padding for the AES algo
    padder = padding.PKCS7(128).padder()
    padded_password = padder.update(password.encode()) + padder.finalize()

    # Encrypte the password
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_password = encryptor.update(padded_password) + encryptor.finalize()

    # Encode it in base64 for the database
    password_b64 = base64.b64encode(encrypted_password).decode()
    salt_b64 = base64.b64encode(salt).decode()
    iv_b64 = base64.b64encode(iv).decode()

    return password_b64, salt_b64, iv_b64


def decrypte_password(encrypted_password, master_password: str, salt: str, iv) -> str:
    key = derive_aes_key(master_password, salt)

    # Decrypte the AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plain_password = decryptor.update(encrypted_password) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    plain_password = unpadder.update(padded_plain_password) + unpadder.finalize()

    return plain_password.decode()


def derive_aes_key(master_password, salt):
    kdf: PBKDF2HMAC = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32,
        backend=default_backend(),
    )
    return kdf.derive(master_password.encode())
