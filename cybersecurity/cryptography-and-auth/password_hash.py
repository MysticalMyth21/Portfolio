import bcrypt

def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def main():
    user_password = input("Enter your password: ")
    hashed_password = hash_password(user_password)
    print(f"Your hashed password is: {hashed_password.decode('utf-8')}")

if __name__ == "__main__":
    main()
