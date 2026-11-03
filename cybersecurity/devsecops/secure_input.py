import re

def collect_data():
    ''' Collects user input safely with 
     protection against buffer overflow and malicious input. '''
    data = "" # Holds all validated input
    MAX_TOTAL = 500 # Max total characters allowed
    MAX_SINGLE = 100 # Max characters per single entry

    while True:
        try: 
            # Get user input
            part = input("Enter text (or 'q' to quit'): ")
            # Allow user to quit
            if part.lower() == 'q':
                break
            # This makes input safe before we use it
            data += part
            part = re.sub(r'\s+', ' ', part)
            # These chars can be used for code injection or break storage
            for c in [';', '<', '>', '[', ']', '{', '}', '$','`', '|', '&']:
                part = part.replace(c,'') # Replace with nothing
            # If sanitization removed everything, skip it
            if not part:
                print ("Warning: Input was empty after cleaning, skipped.")
                continue
            # Check if single input is valid before adding 
            # Reject extremely large single inputs
            if len(part) > MAX_SINGLE: # Check if single input too long
                print (f"Error: Too long! Max {MAX_SINGLE} chars at once. You entered {len(part)}.")
                continue 
            if not any(ch.isalpha() for ch in part): # must contian a letter
                print("Error: Must contain letters.")
                continue
            if len(data) + len(part) >= MAX_TOTAL: # would exceed total limit
                print(f"Limit rachedd! Max {MAX_TOTAL} total.")
                break
            # add safe input to data
            data += part
            print(f"Current total: {len(data)}/{MAX_TOTAL}")
            if len(data) >= MAX_TOTAL: # STOP IF FULL
                print(f"Maximum {MAX_TOTAL} reached.")
                break
        except KeyboardInterrupt: # User pressed Ctrl+C
            print ("\nStopped by user. Exciting safely.")
            break
        except EOFError: # Input ended unexpectedly
            print("\nInput ended. Exiting safely")
            break
        except UnicodeDecodeError: # Encoding problem
            print ("Encoding error. Try agaoin.")
            continue
        except MemoryError: # Out of memory
            print("Low memory. Exiting safely.")
            break
        except Exception as e: # Any other error
            print(f"Error: {e}. Continuing safely.")
            continue
        
    print("Final length:", len(data))
    return data
# This part runs the function
if __name__ == "__main__":
    collect_data() # Start the program
