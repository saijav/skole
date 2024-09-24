import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Parameters
g = 5
p = 37

# Generate random private keys for Alice and Bob
a = random.randint(1, p - 1)  # Alice's private key
print(f"Alices random number a: {a}")
b = random.randint(1, p - 1)  # Bob's private key
print(f"Bobs random number b: {b}")

# Compute public keys
A = pow(g, a, p)  # Alice's public key
print(f"Alices public key A: {A}")
B = pow(g, b, p)  # Bob's public key
print(f"Bobs public key B: {B}")

# Compute shared secret
S_Alice = pow(B, a, p)  # Alice's computed shared secret
print(f"Alices shared final key: {S_Alice}")
S_Bob = pow(A, b, p)    # Bob's computed shared secret
print(f"Bobs shared final key: {S_Bob}")

# The shared secret should be the same
assert S_Alice == S_Bob, "The shared secrets do not match!"

# Hash the shared secret to create a 128-bit (16 bytes) key
shared_secret = S_Alice
hashed_key = hashlib.sha256(str(shared_secret).encode()).digest()[:16]  # 128-bit key
print(f"The hashed key: {hashed_key}")

# Encrypt and decrypt a dummy message using AES
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv  # Get the initialization vector
    encrypted_message = cipher.encrypt(pad(message.encode(), AES.block_size))
    return iv + encrypted_message  # Prepend IV to the message for decryption

def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message[AES.block_size:]), AES.block_size)
    return decrypted_message.decode()

# Dummy message to encrypt
message = "This is a dummy message to encrypt and then decrypt"
print(f"Original message: {message}")

# Encrypt the message
encrypted_message = encrypt_message(message, hashed_key)
print(f"Encrypted message: {encrypted_message.hex()}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, hashed_key)
print(f"Decrypted message: {decrypted_message}")

