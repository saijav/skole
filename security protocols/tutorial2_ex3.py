import hashlib


def main():
    file_path = "sample.txt"

    # create txt file
    with open(file_path, "w") as file:
        file.write("This text will be encrypted and decrypted using SHA256")
    print(f"File '{file_path}' created with initial content.")

    # compute sha256 of the file
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        original_hash = sha256.hexdigest()
        print(f"Original SHA-256 Digest of the file '{file_path}': {original_hash}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return

    # modify the file
    with open(file_path, "r") as file:
        content = file.read()

    modified_content = content.replace("This", "this")

    with open(file_path, "w") as file:
        file.write(modified_content)
    print(f"File '{file_path}' modified by changing 'This' to 'this'.")

    # compute sha256 of the modified file
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        modified_hash = sha256.hexdigest()
        print(f"Modified SHA-256 Digest of the file '{file_path}': {modified_hash}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return

    # observe what happens to the hashes
    if original_hash != modified_hash:
        print("The file has been modified; hashes do not match.")
    else:
        print("The file is unchanged; hashes match.")


if __name__ == "__main__":
    main()
