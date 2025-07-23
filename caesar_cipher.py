def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97
            if mode == 'E':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'D':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Leave spaces, digits, and symbols unchanged

    return result

# Main Program
print("=== Caesar Cipher Program ===")
choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()

if choice not in ['E', 'D']:
    print("Invalid choice. Please enter E for encryption or D for decryption.")
else:
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g., 3): "))

    output = caesar_cipher(message, shift, choice)

    if choice == 'E':
        print("🔐 Encrypted Message:", output)
    else:
        print("🔓 Decrypted Message:", output)