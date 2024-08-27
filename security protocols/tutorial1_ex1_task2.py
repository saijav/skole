import time

#validate the shift number K
def validate_k(k):
    try:
        k = int(k)
        if 0 <= k < 26:
            return k
        else:
            print("Invalid K. Please enter a number between 0 and 25.")
            return None
    except ValueError:
        print("Invalid K. Please enter a valid integer.")
        return None

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
    while True:
        k = validate_k(input("Enter the shift number K (0-25): "))
        if k is not None:
            break

    #choose operation
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if mode == 'e':
        plaintext = input("Enter the plaintext to encrypt: ")
        start_time = time.time()
        ciphertext = encrypt(plaintext, k)
        end_time = time.time()
        print(f"Ciphertext: {ciphertext}")
        print(f"Encryption time: {end_time - start_time} seconds")
    elif mode == 'd':
        ciphertext = input("Enter the ciphertext to decrypt: ")
        start_time = time.time()
        plaintext = decrypt(ciphertext, k)
        end_time = time.time()
        print(f"Plaintext: {plaintext}")
        print(f"Decryption time: {end_time - start_time} seconds")
    else:
        print("Invalid mode. Please select either 'E' for encrypt or 'D' for decrypt.")

caesar_cipher()
