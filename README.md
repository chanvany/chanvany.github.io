# Caesar Cipher Tool
A simple Python desktop application which is a Caesar Cipher tool that allows the user to encrypt and decrypt messages with a random shift value, while also providing extra security with a PIN code.

## Features

- Encryption with a random shift key (Caesar Cipher)

- Security with a PIN that is required for decryption

- Decryption capability after entering the correct PIN

- Non-technical user interaction that allows users to easily encrypt and decrypt messages

## Functions
- key = random.randint(1, 25)

-Purpose: This line generates a random integer between 1 and 25, which will be used as the shift key for the Caesar cipher encryption. This means the message will be encrypted by shifting each letter or number by a random number of positions

- if char.isalpha():
    base = ord('A') if char.isupper() else ord('a')
    encrypted += chr((ord(char) - base + shift) % 26 + base):

-Purpose: This checks if the character is a letter and then shifts it by the shift value. It handles both uppercase and lowercase letters.

- elif char.isdigit():
    encrypted += str((int(char) + shift) % 10)

-Purpose: This checks if the character is a digit and shifts it by the shift value. It ensures digits loop around from 9 to 0 when needed (e.g., 8 + 3 = 1).

- while len(user_pin) != 4 or not user_pin.isdigit():
    user_pin = input(" PIN must be exactly 4 digits. Try again: ")

-Purpose: This ensures that the user enters a valid 4-digit PIN. If the input is invalid (not 4 digits or contains non-numeric characters), the program asks again.

- if entered_pin == user_pin:
    decrypted_message = caesar_decrypt(encrypted_message, key)
  
-Purpose: This checks if the entered PIN matches the PIN the user set earlier. If it’s correct, the program proceeds to decrypt the message using the correct shift value.

- else:
    encrypted += char

-Purpose: This part of the code ensures that non-alphabetic characters (like punctuation, spaces, etc.) are left unchanged during encryption and decryption.

- choice = input("\nDo you want to decrypt your message? (y/n): ").lower()

-Purpose: This asks the user if they want to decrypt their message, and converts the input to lowercase for consistency (handles both 'y' and 'Y').

- print(" Encrypted Message:", encrypted_message)
print(" Encryption Key (Save this to decrypt):", key)

-Purpose: After encrypting the message, this displays:
- The encrypted message.
- The key used for encryption (which is required for decryption).



## How to Run

1. Make sure you have Python 3 installed.  
2. Clone the repository:  
   ```bash
   git clone https://github.com/chanvany/chanvany.github.io
