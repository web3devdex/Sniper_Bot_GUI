from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, padding, hmac
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
import os
import base64


class Encryption:
    def __init__(self):
        self.masterkey = None  # Initialize masterkey to None
        
    def generate_masterkey(self, password):
        self.masterkey = self.derivation_masterkey(password).hex()

    def derivation_masterkey(self, key):
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32, 
            salt=None,  
            info=b'encryption-context-data',
            backend=default_backend()
        )
        return hkdf.derive(key)

    def derive_key(self, password: str, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend(),
        )
        return kdf.derive(password.encode())

    def encrypt(self, plaintext: str, password: str) -> str:
        salt = os.urandom(16)
        iv = os.urandom(16)
        key = self.derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        if not isinstance(plaintext, bytes):
            plaintext = plaintext.encode()
        padded_data = padder.update(plaintext) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        h.update(iv + ciphertext)
        hmac_value = h.finalize()
        return base64.b64encode(salt + iv + ciphertext + hmac_value).decode("utf-8")


    def decrypt(self, ciphertext: str, password: str) -> str:
        try:
            decoded_data = base64.b64decode(ciphertext)
            salt = decoded_data[:16]
            iv = decoded_data[16:32]
            ciphertext = decoded_data[32:-32]
            hmac_value = decoded_data[-32:]
            key = self.derive_key(password, salt)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
            h.update(iv + ciphertext)
            h.verify(hmac_value)
            return plaintext.decode("utf-8")
        except (ValueError, KeyError):
            raise ValueError("Decryption failed. Invalid password or corrupted data.")
        except InvalidSignature:
            raise ValueError("Decryption failed. HMAC verification failed.")

    def verify_password(self, ciphertext: str, password: str) -> bool:
        try:
            self.decrypt(ciphertext, password)
            return True
        except ValueError:
            return False
        
    
    def change_password(
        self, old_password: str, new_password: str, ciphertext: str
    ) -> str:
        if not self.verify_password(ciphertext, old_password):
            raise ValueError("Old password is incorrect.")
        plaintext = self.decrypt(ciphertext, old_password)
        return self.encrypt(plaintext, new_password)
