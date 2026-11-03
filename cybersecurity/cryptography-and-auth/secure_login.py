import hashlib # for secure hashing
import os # to generate random salt
import re # for username validation

users = {} # dictionary to store user data

def validate_input(username, password):
    # Validate user input 
    if not username or not username.strip():
        return False, "Username cannot be empty."

    if not password or not password.strip():
        return False, "Password cannot be empty."

    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.match("^[a-zA-Z0-9_]+$", username):
        return False, "Username can only contain letters, numbers, and underscores."
    
    return True, ""

def hash_password(password):
    # Create secure hash with salt
    # Generate 16-byte random salt
    salt = os.urandom(16)
    # Hash password with salt using PBKDF2, 100000 iterations
    hash_val = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Store salt + hash together so we can verify later
    return salt + hash_val

def verify_password(stored, password):
    # Verify passwrod against stored salt+hash
    # First 16 bytes is the salt
    salt = stored[:16]
    # Rest is the original hash
    stored_hash = stored[16:] 
    # Hash the provided password with the stored salt
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Compare hashes
    return new_hash == stored_hash

def register():
    # Handle user registration
    try:
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()

        # Validate input
        valid, msg = validate_input(username, password)

        if not valid:
            print(f"Registration failed: {msg}")
            return

        # Prevent overwriting existing user
        if username in users:
            print("Invalid credentials: Username already exists.")
            return

        # Hash password securely instead of storing plain text
        users[username] = hash_password(password)
        print("User Registered Successfully!")

    except Exception:
        print("An error occurred during registration. Please try again.")

def login():
    # Handle user login
    try:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        # Check empty
        if not username or not password:
            print("Invalid credentials.")
            return

        # Generic message - don't reveal if user exists or not
        if username not in users:
            print("Invalid credentials.")
            return

        # Verify password 
        stored = users[username]
        if verify_password(stored, password):
            print("Login Successful!")
        else:
            print("Invalid credentials.")

    except Exception:
        print("An error occurred during login. Please try again.")

def main():
    # Main menu loop
    while True:
        print("\nWelcome to the User Authentication System\n1, Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            register()

        elif choice == '2':
            login()

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()
