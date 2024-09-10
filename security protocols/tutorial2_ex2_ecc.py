from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import time

def main():
    name = input("Enter name: ")

    # Generate ECC private and public keys
    private_key = ec.generate_private_key(
        ec.SECP384R1(), backend=default_backend()
    )
    public_key = private_key.public_key()

    # Save the private key
    with open(f"{name}_ECC_Private_Key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save the public key
    with open(f"{name}_ECC_Public_Key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print(f"ECC key pair generated")

    message = "This is a one paragraph of text that will be encrypted"

    # Signing (acting as encryption)
    start_time = time.time()
    signature = private_key.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    end_time = time.time()
    print(f"ECC encryption time: {end_time - start_time:.6f} seconds")

    # Verification (acting as decryption)
    start_time = time.time()
    try:
        public_key.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        verification_result = "decrypted."
    except Exception as e:
        verification_result = f"decryption failed: {str(e)}"
    end_time = time.time()
    print(f"ECC decryption time: {end_time - start_time:.6f} seconds")
    print(verification_result)

if __name__ == "__main__":
    main()
