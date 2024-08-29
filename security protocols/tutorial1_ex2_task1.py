import time

#encryption
def encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            new_char = chr(((ord(char) - shift + k) % 26) + shift)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

#decryption
def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k % 26)


def caesar_cipher():
    plaintext = input("Enter the plaintext to encrypt: ")
    start_time = time.time()
    ciphertext = encrypt(plaintext, 13)
    plaintext = decrypt(ciphertext, 9)
    print(f"Plaintext: {plaintext}")
    end_time = time.time()
    print(f"Decryption time: {end_time - start_time} seconds")
caesar_cipher()