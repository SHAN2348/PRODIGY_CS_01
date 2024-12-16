def caesar_cipher(message, shift, direction):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    Args:
        message (str): The text to be encrypted or decrypted.
        shift (int): The shift value for the Caesar Cipher.
        direction (str): 'encrypt' or 'decrypt'.

    Returns:1
        str: The encrypted or decrypted message.
    """
    result = ""

    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift_amount = shift if direction == 'encrypt' else -shift
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char

    return result

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            message = input("Enter a message to encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_message = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter a message to decrypt: ")
            shift = int(input("Enter the shift value used for encryption: "))
            decrypted_message = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()