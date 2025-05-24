from PIL import Image
import random

# Function to encrypt an image using a mathematical operation (addition) and pixel swapping
def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Load image pixels

    width, height = image.size
    encrypted_pixels = []

    # Encrypt the pixels by adding the key to the RGB values
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_r = (r + key) % 256  # Ensure the result stays in the 0-255 range
            encrypted_g = (g + key) % 256
            encrypted_b = (b + key) % 256
            encrypted_pixels.append((encrypted_r, encrypted_g, encrypted_b))
            pixels[i, j] = (encrypted_r, encrypted_g, encrypted_b)

    # Save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    image.save(encrypted_image_path)
    print(f"Encrypted image saved at: {encrypted_image_path}")
    return encrypted_image_path

# Function to decrypt an image by subtracting the key from the RGB values
def decrypt_image(image_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    pixels = image.load()  # Load image pixels

    width, height = image.size
    decrypted_pixels = []

    # Decrypt the pixels by subtracting the key from the RGB values
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_r = (r - key) % 256  # Reverse the encryption by subtracting the key
            decrypted_g = (g - key) % 256
            decrypted_b = (b - key) % 256
            decrypted_pixels.append((decrypted_r, decrypted_g, decrypted_b))
            pixels[i, j] = (decrypted_r, decrypted_g, decrypted_b)

    # Save the decrypted image
    decrypted_image_path = "decrypted_image.png"
    image.save(decrypted_image_path)
    print(f"Decrypted image saved at: {decrypted_image_path}")
    return decrypted_image_path

# Function to swap pixels randomly for encryption
def swap_pixels(image_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Load image pixels

    width, height = image.size

    # Randomly swap pixels to encrypt the image
    for i in range(width):
        for j in range(height):
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            temp = pixels[i, j]
            pixels[i, j] = pixels[x, y]
            pixels[x, y] = temp

    # Save the encrypted image after pixel swap
    swapped_image_path = "swapped_encrypted_image.png"
    image.save(swapped_image_path)
    print(f"Swapped encrypted image saved at: {swapped_image_path}")
    return swapped_image_path

# Main function to run the program
def main():
    print("Welcome to the Image Encryption Tool!")
    action = input("Do you want to (E)ncrypt, (D)ecrypt, or (S)wap pixels? ").lower()
    image_path = input("Enter the path of the image: ")

    if action == 'e':
        key = int(input("Enter a key (an integer for encryption): "))
        encrypt_image(image_path, key)
    elif action == 'd':
        key = int(input("Enter the key for decryption: "))
        decrypt_image(image_path, key)
    elif action == 's':
        swap_pixels(image_path)
    else:
        print("Invalid choice. Please enter 'E' for encryption, 'D' for decryption, or 'S' for swapping pixels.")

# Run the program
if __name__ == "__main__":
    main()