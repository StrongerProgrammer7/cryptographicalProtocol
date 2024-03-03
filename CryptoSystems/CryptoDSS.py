import sys

from CryptoSystems.CryptoSystems import CryptoSystems
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend


class CryptoDSS(CryptoSystems):

    def __init__(self, filePath, keySize=1024, hash512=False):
        super().__init__()
        self.public_key = None
        self.private_key = None
        self.keySize = keySize
        self.hash512 = hash512
        self._readFile(filePath)

    def _readFile(self, filePath):
        try:
            with open(filePath, "rb") as file:
                self.file_content = file.read()
        except OSError:
            print("Could not open/read file:", filePath)
            sys.exit()

    def generate_keypair(self):
        self.private_key = dsa.generate_private_key(
            key_size=self.keySize,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        # return private_key, public_key

    def sign_file(self, private_key):
        if self.private_key is None or self.public_key is None:
            print("Generate key pair!!")
            return None
        signature = private_key.sign(
            self.file_content,
            self._getHash()
        )
        return signature

    def verify_signature(self, public_key, signature):
        try:
            public_key.verify(
                signature,
                self.file_content,
                self._getHash()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False

    def _getHash(self):
        if self.hash512:
            return hashes.SHA512()
        else:
            return hashes.SHA256()
