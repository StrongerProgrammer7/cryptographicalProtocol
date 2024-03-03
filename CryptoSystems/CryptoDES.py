from Cryptodome.Cipher import DES

from CryptoSystems.CryptoSystems import CryptoSystems
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

class CryptoDES(CryptoSystems):

    def __init__(self, MODE):
        super().__init__(MODE)

    def encrypt_des(self,message, key):
        iv = get_random_bytes(8)  # Генерация случайного инициализационного вектора
        cipher = DES.new(key, self.MODE, iv)
        ciphertext = cipher.encrypt(pad(message.encode('utf-8'), DES.block_size))
        return iv + ciphertext

    def decrypt_des(self,ciphertext, key):
        iv = ciphertext[:8]
        ciphertext = ciphertext[8:]
        cipher = DES.new(key, self.MODE, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return decrypted_message.decode('utf-8')



