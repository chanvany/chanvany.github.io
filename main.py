import random

# Function to encrypt a message using Caesar cipher
def caesar_encrypt(text, shift):
    encrypted = ""  # Start with an empty string for the encrypted message
    for char in text:  # Go through each character in the message
        if char.isalpha():  # If the character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Determine if it's uppercase or lowercase
            encrypted += chr((ord(char) - base + shift) % 26 + base)  # Shift letter and add to encrypted string
        elif char.isdigit():  # If the character is a number
            encrypted += str((int(char) + shift) % 10)  # Shift the number and add to encrypted string
        else:  # If it's neither a letter nor a number, leave it unchanged (like punctuation or spaces)
            encrypted += char
    return encrypted  # Return the encrypted message

# Function to decrypt a message using Caesar cipher
def caesar_decrypt(text, shift):
    decrypted = ""  # Start with an empty string for the decrypted message
    for char in text:  # Go through each character in the encrypted message
        if char.isalpha():  # If the character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Determine if it's uppercase or lowercase
            decrypted += chr((ord(char) - base - shift) % 26 + base)  # Shift the letter back and add to decrypted string
        elif char.isdigit():  # If the character is a number
            decrypted += str((int(char) - shift) % 10)  # Shift the number back and add to decrypted string
        else:  # If it's neither a letter nor a number, leave it unchanged
            decrypted += char
    return decrypted  # Return the decrypted message

# --- Main Program ---
print("=== Caesar Cipher Tool ===")  # Print the tool's title

# Encrypting the user's message
message = input("Enter your message to encrypt: ")  # Ask the user for a message
key = random.randint(1, 25)  # Generate a random shift value (key) between 1 and 25
encrypted_message = caesar_encrypt(message, key)  # Encrypt the message using the Caesar cipher

# Show the encrypted message and the key (shift value) used
print("\n Encrypted Message:", encrypted_message)
print(" Encryption Key (Save this to decrypt):", key)

# Setting up a PIN for extra security
user_pin = input("\n Set a PIN for security (4 digits): ")  # Ask the user to set a 4-digit PIN
while len(user_pin) != 4 or not user_pin.isdigit():  # Check if the PIN is exactly 4 digits
    user_pin = input(" PIN must be exactly 4 digits. Try again: ")  # Ask again if it's invalid

print(" PIN set successfully!")  # Confirm that the PIN has been set

# Option to decrypt the message
while True:
    choice = input("\nDo you want to decrypt your message? (y/n): ").lower()  # Ask if the user wants to decrypt
    if choice in ['y', 'yes']:  # If the user wants to decrypt
        entered_pin = input(" Enter your PIN to decrypt: ")  # Ask for the PIN
        if entered_pin == user_pin:  # Check if the PIN matches
            decrypted_message = caesar_decrypt(encrypted_message, key)  # Decrypt the message
            print(" Decrypted Message:", decrypted_message)  # Show the decrypted message
            break  # End the loop after successful decryption
        else:
            print(" Incorrect PIN! Access denied.")  # If the PIN is incorrect, show an error and stop decryption
            break
    elif choice in ['n', 'no']:  # If the user does not want to decrypt
        break
    else:
        print(" Please enter 'y' for yes or 'n' for no.")  # Ask again if the input is not valid

print("\n Thank you for using the Caesar Cipher Tool!")  # Thank the user for using the tool
print(" Goodbye!")  # Say goodbye
