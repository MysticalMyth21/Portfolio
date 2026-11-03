"""
Capstone Project - Ciphers (cipher.py)
This program encodes a user's message using a cyclical Caesar cipher 
that shifts each alphabetical character forward by 15 positions.
"""

def shift_character(char, shift_amount=15):
    """
    Shifts a single alphabetical character by shift_amount using ASCII values.
    Preserves uppercase/lowercase and leaves spaces/punctuation unchanged.
    """
    # Check if the character is an uppercase letter (ASCII 65-90)
    if char.isupper():
        base_ascii = ord('A')
        shifted_ascii = (ord(char) - base_ascii + shift_amount) % 26 + base_ascii
        return chr(shifted_ascii)
    
    # Check if the character is a lowercase letter (ASCII 97-122)
    elif char.islower():
        base_ascii = ord('a')
        shifted_ascii = (ord(char) - base_ascii + shift_amount) % 26 + base_ascii
        return chr(shifted_ascii)
    
    # Spaces, numbers, and punctuation marks remain unchanged
    else:
        return char


def encode_message(message, shift_amount=15):
    """
    Takes a plain text string and returns the encoded cipher string.
    """
    encoded_chars = [shift_character(char, shift_amount) for char in message]
    return "".join(encoded_chars)


def display_results(original_message, encoded_message, shift_amount=15):
    """
    Prints the original and encoded messages in a clean, user-friendly format.
    """
    separator = "-" * 60
    print(f"\n{separator}")
    print(f"{'Cipher Shift:':<22} +{shift_amount} positions")
    print(f"{'Original Message:':<22} {original_message}")
    print(f"{'Encoded Message:':<22} {encoded_message}")
    print(f"{separator}\n")


def main():
    """
    Main function to get user input, encode the message, and display output.
    """
    print("=" * 60)
    print("                CAESAR CIPHER ENCODER (+15)                 ")
    print("=" * 60)
    
    user_message = input("\nPlease enter the message you would like to encode:\n> ")
    
    # Encode the message using a shift of 15
    secret_message = encode_message(user_message, shift_amount=15)
    
    # Display well-formatted, labelled output
    display_results(user_message, secret_message, shift_amount=15)


if __name__ == "__main__":
    main()
