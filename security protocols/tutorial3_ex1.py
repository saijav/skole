import rsa
import time
import hashlib


def main():
    name = input("Enter name: ")
    public_key, private_key = rsa.newkeys(1024)
    file_path = "sample.txt"

    # Save the public and private keys to files
    with open(f"{name}_Public_key.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open(f"{name}_Private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

    print(f"RSA key pair generated")

    message = "This is a one paragraph of text that will be encrypted and signed"

    # Message to be encrypted and signed
    with open(file_path, "w") as file:
        file.write(message)
    print(f"File '{file_path}' created with initial content.")

    # encrypt
    start_time = time.time()
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    end_time = time.time()
    print(f"RSA encryption time: {end_time - start_time:.6f} seconds")

    with open("encrypted.message", "wb") as f:
        f.write(encrypted_message)

    # decrypt
    start_time1 = time.time()
    clear_message = rsa.decrypt(encrypted_message, private_key)
    end_time1 = time.time()
    print(f"Decrypted message: {clear_message.decode()}")
    print(f"RSA decryption time: {end_time1 - start_time1:.6f} seconds")

    # sign
    # Hash the message
    message_hash = hashlib.sha256(message.encode()).digest()

    # Sign the hashed message with the private key
    signature = rsa.sign(message_hash, private_key, 'SHA-256')

    # Save the signature to a file
    with open("signature.sig", "wb") as f:
        f.write(signature)

    print("Message signed and signature saved to 'signature.sig'")

    # verification
    # Load the signature from the file
    with open("signature.sig", "rb") as f:
        loaded_signature = f.read()

    # Hash the clear message again for verification
    verification_message_hash = hashlib.sha256(clear_message).digest()

    try:
        rsa.verify(verification_message_hash, loaded_signature, public_key)
        print("Signature is valid!")
    except rsa.VerificationError:
        print("Signature is invalid!")


if __name__ == "__main__":
    main()
