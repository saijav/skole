import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import time

def generate_key():
    key = os.urandom(32)
    return key

def encrypt(plaintext, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt(ciphertext, key):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

def symmetric_cipher():
    # Generate a symmetric key
    key = generate_key()
    print(f"Generated AES-256 Key: {key.hex()}\n")

    plaintext = input("Enter text to encrypt: ")

    # Measure the time taken to encrypt
    start_time = time.time()
    ciphertext = encrypt(plaintext, key)
    encryption_time = time.time() - start_time
    print(f"\nCiphertext (hex): {ciphertext.hex()}")
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Measure the time taken to decrypt
    start_time = time.time()
    decrypted_text = decrypt(ciphertext, key)
    decryption_time = time.time() - start_time
    print(f"\nDecrypted Text: {decrypted_text}")
    print(f"Decryption Time: {decryption_time:.6f} seconds")

symmetric_cipher()
