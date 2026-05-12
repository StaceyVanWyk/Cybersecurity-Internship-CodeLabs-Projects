"""
Simple Caesar Cipher Program

This program demonstrates basic encryption and decryption
using the Caesar Cipher technique.

Concepts learned:
- IPO Model
- Data Confidentiality
- ASCII manipulation
- Encryption & Decryption logic
"""

UPPERCASE_OFFSET = 65
LOWERCASE_OFFSET = 97
ALPHABET_SIZE = 26


def encrypt(message, shift):
    """Encrypt a message using Caesar Cipher."""
    result = ""

    for char in message:
        if char.isupper():
            shifted = (
                ord(char) - UPPERCASE_OFFSET + shift
            ) % ALPHABET_SIZE + UPPERCASE_OFFSET

            result += chr(shifted)

        elif char.islower():
            shifted = (
                ord(char) - LOWERCASE_OFFSET + shift
            ) % ALPHABET_SIZE + LOWERCASE_OFFSET

            result += chr(shifted)

        else:
            # Preserve spaces and punctuation
            result += char

    return result


def decrypt(message, shift):
    """Decrypt a message using Caesar Cipher."""
    result = ""

    for char in message:
        if char.isupper():
            shifted = (
                ord(char) - UPPERCASE_OFFSET - shift
            ) % ALPHABET_SIZE + UPPERCASE_OFFSET

            result += chr(shifted)

        elif char.islower():
            shifted = (
                ord(char) - LOWERCASE_OFFSET - shift
            ) % ALPHABET_SIZE + LOWERCASE_OFFSET

            result += chr(shifted)

        else:
            # Preserve spaces and punctuation
            result += char

    return result


def main():
    """Run the Caesar Cipher program."""

    user_message = input("Please enter your message: ")

    try:
        shift = int(input("Enter shift value: "))

    except ValueError:
        print("Shift value must be a number.")
        return

    encrypted_message = encrypt(user_message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print("\nResults")
    print("Original Message :", user_message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()
