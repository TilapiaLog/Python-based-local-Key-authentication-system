from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

class AESCipher:
    def __init__(self, key):
        self.key = key.encode('utf-8').ljust(32)[:32]
        self.iv = hashlib.sha256(self.key).digest()[:16]

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return ct 

    def decrypt(self, ciphertext, iv):
        iv_bytes = bytes.fromhex(iv)
        cipher = AES.new(self.key, AES.MODE_CBC, iv_bytes)
        ct = base64.b64decode(ciphertext)
        plaintext = unpad(cipher.decrypt(ct), AES.block_size)
        return plaintext.decode('utf-8')