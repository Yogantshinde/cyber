 #Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ''
    
    # Iterate over each character in the text
    for char in text:
        if char.isalpha():
            # Check if character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Shift character and wrap around if needed
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # If it's not a letter, just add the character as is
            result += char
    
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    result = ''
    
    # Iterate over each character in the text
    for char in text:
        if char.isalpha():
            # Check if character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Reverse the shift and wrap around if needed
            result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            # If it's not a letter, just add the character as is
            result += char
    
    return result

# Main function to run the program
def main():
    print("Welcome to the Caesar Cipher!")
    
    # Ask for user input
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter either 'E' to encrypt or 'D' to decrypt.")

# Run the program
if __name__ == "__main__":
    main()