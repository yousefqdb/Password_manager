from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

from functions.json import *

class crypt:
    def encrypt(message):
        key = get_enc_key()
        key = key.ljust(32)
        key = key.encode('utf-8')
        message = message.encode('utf-8')
    
        iv = b'\0' * 16  
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
    
        ciphertext = encryptor.update(message) + encryptor.finalize()
        return b64encode(iv + ciphertext).decode('utf-8')

    def decrypt(message):
        key = get_enc_key()
        key = key.ljust(32)
        key = key.encode('utf-8')
        message = b64decode(message.encode('utf-8'))
    
        iv = message[:16]
        message = message[16:]
    
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
    
        message = decryptor.update(message) + decryptor.finalize()
        return message.decode('utf-8')