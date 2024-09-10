import rsa
import time

def main():
    name = input("Enter name: ")
    public_key, private_key = rsa.newkeys(1024)


    with open(f"{name}_Public_key.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open(f"{name}_Private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

    print(f"RSA key pair generated")

    message = "This is a one paragraph of text that will be encrypted"

    start_time = time.time()
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    end_time = time.time()
    print(f"RSA encryption time: {end_time-start_time:.6f} seconds")

    with open("encrypted.message", "wb") as f:
        f.write(encrypted_message)

    start_time1 = time.time()
    clear_message = rsa.decrypt(encrypted_message, private_key)
    end_time1 = time.time()

    print(clear_message.decode())
    print(f"RSA decryption time: {end_time1 - start_time1:.6f} seconds")

if __name__ == "__main__":
    main()




