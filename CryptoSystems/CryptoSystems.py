
from Cryptodome.Random import get_random_bytes

from Cryptodome.Cipher import DES

class CryptoSystems:

    def __init__(self, MODE="DES.CBC"):
        if MODE == "DES.CBC":
            self.MODE = DES.MODE_CBC
        elif MODE == "DES.CFB":
            self.MODE = DES.MODE_CFB

    def generateKey(self,length):
        return get_random_bytes(length)

