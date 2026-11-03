from cryptography.fernet import Fernet

def encrypt(text, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode('utf-8'))
    return encrypted_text

def decrypt(encrypted_text, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text).decode('utf-8')
    return decrypted_text

def main():
    key = Fernet.generate_key()
    print(f"Generated Key: {key.decode()}")
    user_text = input("Enter text to encrypt: ")
    encrypted = encrypt(user_text, key)
    print(f"Encrypted {encrypted.decode()}")
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
