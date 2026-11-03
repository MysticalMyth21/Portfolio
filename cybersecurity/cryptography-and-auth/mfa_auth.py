import hashlib
import hmac
import base64
import struct
import time

# ==============================
# Configuration / Stored Values
# ==============================

# Choose your own password and biometric key, then generate hashes
# using the helper snippet shown in the task instructions.
STORED_PASSWORD_HASH = "a109e36947ad56de1dca1cc49f0ef8ac9ad9a7b1aa0df41fb3c4cb73c1ff01ea"       # Password: "Password123!""
STORED_BIOMETRIC_HASH = "d7cabdb198fe236226b75bdb81a445ac04b3c2ceef5246fa9467d5adb5682927"      # Biometric: "faceid"

# Base32 TOTP secret (20-byte secret encoded in base32).
# You can use this default or replace with your own.
TOTP_SECRET = "JBSWY3DPEHPK3PXP"  # Example base32 string

 
# ==============================
# Helper Functions
# ==============================

def hash_input(input_text: str) -> str:
    """
    Hash input using SHA-256 and return the hexadecimal result.
    """

    return hashlib.sha256(input_text.encode()).hexdigest()




def generate_totp(secret: str, interval: int = 30, digits: int = 6) -> str:
    """
    Generate a Time-based One-Time Password (TOTP) using HMAC-SHA1.
    Do not modify this function. You will call it from verify_otp().
    """
    # Decode base32 secret
    key = base64.b32decode(secret, casefold=True)

    # Get current Unix time and compute the time step (counter)
    timestep = int(time.time() // interval)

    # Pack timestep into 8-byte big-endian
    msg = struct.pack(">Q", timestep)

    # HMAC-SHA1
    hmac_digest = hmac.new(key, msg, hashlib.sha1).digest()

    # Dynamic truncation
    offset = hmac_digest[-1] & 0x0F
    code = ((hmac_digest[offset] & 0x7F) << 24 |
            (hmac_digest[offset + 1] & 0xFF) << 16 |
            (hmac_digest[offset + 2] & 0xFF) << 8 |
            (hmac_digest[offset + 3] & 0xFF))

    # Reduce to the desired number of digits
    otp = code % (10 ** digits)
    return str(otp).zfill(digits)


# ==============================
# Verification Functions
# ==============================

def verify_password() -> bool:
    """
    Prompt for a password and verify it against STORED_PASSWORD_HASH.
    """
    password = input("Enter your password: ")
    hashed = hash_input(password)
    if hmac.compare_digest(hashed, STORED_PASSWORD_HASH):
        return True
    return False

def verify_otp() -> bool:
    """
    Generate a TOTP code using generate_totp() and
    verify user input against it.
    """
    current_code = generate_totp(TOTP_SECRET)
    print (f"\nCurrent TOTP code : {current_code}")
    # 2. Prompt the user for the TOTP
    user_code = input("\nEnter your 6-digit TOTP code: ").strip()

    # 3. Compare user input with generated code
    if user_code == current_code:
        return True
    else:
        print("\nInvalid TOTP. Please check your authenticator code.")
        return False


def verify_biometric() -> bool:
    """
    Simulate biometric check by hashing user input and comparing
    with STORED_BIOMETRIC_HASH.
    """
    bio_key = input("\nEnter your biometric key: ")
    hashed_bio = hash_input(bio_key)
    if hmac.compare_digest(hashed_bio, STORED_BIOMETRIC_HASH):
        return True
    return False

# ==============================
# Main Authentication Flow
# ==============================

def main():
    """
    Main function to run the MFA system, requiring all three factors to pass.
    """
    print("\nWelcome to the MFA Authentication System\n")
    print("You must pass all three authentication factors.\n")

    # Step 1: Password verification
    if not verify_password():
        print("Authentication failed: Password verification failed.\n")
        return

    # Step 2: TOTP verification
    if not verify_otp():
        print("Authentication failed: TOTP verification failed.\n")
        return

    # Step 3: Biometric verification
    if not verify_biometric():
        print("Authentication failed: Biometric verification failed.\n")
        return

    # If all checks pass:
    print("Authentication successful! Access granted.\n")


if __name__ == "__main__":
    main()
