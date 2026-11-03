"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
class Email:

    def __init__ (self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True
# instance variable for a specific object from False to True.


# --- Functions --- #
# Build out the required functions for your program.

inbox = []

def populate_inbox():
      email1 = Email ("welcome@hyperiondev.com", "Welcome to HyperionDev!","Hello and welcome to HyperionDev.")
      email2 = Email ("careers@hyperiondev.com", "Great work on the bootcamp!", "You have done an amazing job.")
      email3 = Email ("marks@hyperiondev.com", "Your excellent marks!", "You scored 100% on your task!")
      inbox.append (email1)
      inbox.append (email2)
      inbox.append (email3)

def list_emails():
    for index, email in enumerate (inbox):
        print (f"{index} {email.subject_line}")

def read_email(index):
    try:
        email = inbox [index]
        print (f"\n--- Email {index} ---")
        print (f"From: {email.email_address}")
        print (f"Subject: {email.subject_line}")
        print (f"Content: {email.email_content}\n")

        email.mark_as_read()
        print (f"Email from {email.email_address} marked as read.\n")
    except IndexError:
        print ("Oops - Incorrect index. That email does not exist.\n")

def view_unread_emails():
    print ("\nUnread emails:")
    unread_found = False
    
    for index, email in enumerate (inbox):
        if not email.has_been_read:
            print (f"{index} {email.subject_line}")
            unread_found = True

    if not unread_found:
        print ("No unread emails.")
    print()

populate_inbox()
    
while True:
    try:
        user_choice = int(input("""\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application
        
        Enter selection:"""))

        if user_choice == 1:
            list_emails()
            try:
                email_index = int(input("\nEnter the index of the email you want to read: "))
                read_email (email_index)
            except ValueError:
                print ("Oops - Incorrect input. Please enter a number.\n")
        elif user_choice == 2:
            view_unread_emails()
        elif user_choice == 3:
            print ("Goodbye!")
            break
        else:
            print ("Oops - Incorrect input.")
    except ValueError:
        print ("Oops - Incorrect input. Please enter 1, 2 or 3.")
