# -*- coding: utf-8 -*-
"""DataEncryptionStandard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VlDKB1IT9gOUMMmce3P6MZM70HRNXR1H
"""

# BIBLIOTECA UTILIZADA ->PyCryptodome
!pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def des_encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = des.encrypt(padded_text)
    return binascii.hexlify(ciphertext).decode('utf-8')

def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    encrypted_text = binascii.unhexlify(ciphertext)
    decrypted_text = des.decrypt(encrypted_text)
    return decrypted_text.rstrip(b' ').decode('utf-8')

# Entrada do usuário
plaintext = input("Digite o texto a ser cifrado: ").encode('utf-8')
key = get_random_bytes(8)  # Chave deve ter 8 bytes (64 bits)

print("Texto original:", plaintext.decode('utf-8'))

ciphertext = des_encrypt(plaintext, key)
print("Texto cifrado:", ciphertext)

decrypted_text = des_decrypt(ciphertext, key)
print("Texto decifrado:", decrypted_text)

