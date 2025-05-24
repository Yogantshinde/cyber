import re

# Function to check the strength of the password
def check_password_strength(password):
    strength = 0
    
    # Check password length (should be at least 8 characters)
    if len(password) >= 8:
        strength += 1
    
    # Check if the password has at least one lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Check if the password has at least one uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Check if the password has at least one digit
    if re.search(r'[0-9]', password):
        strength += 1
    
    # Check if the password has at least one special character
    if re.search(r'[\W_]', password):
        strength += 1
    
    # Provide feedback based on the strength score
    if strength == 5:
        return "Strong", "Your password is very strong!"
    elif strength == 4:
        return "Moderate", "Your password is moderate. Consider adding more variety."
    else:
        return "Weak", "Your password is weak. Consider making it longer and adding more complexity."

# Function to interact with the user
def main():
    print("Welcome to the Password Strength Checker!")
    
    # Get the password from the user
    password = input("Please enter your password: ")
    
    # Check password strength
    strength, message = check_password_strength(password)
    
    # Display feedback to the user
    print(f"Password Strength: {strength}")
    print(message)

# Run the program
if __name__ == "__main__":
    main()