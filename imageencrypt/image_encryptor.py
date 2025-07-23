def encrypt_decrypt_image(filename, key, mode):
    with open(filename, 'rb') as f:
        image_data = bytearray(f.read())

    for i in range(len(image_data)):
        image_data[i] ^= key  # XOR encryption/decryption

    if mode == "encrypt":
        new_filename = f"encrypted_{filename}"
    elif mode == "decrypt":
        if filename.startswith("encrypted_"):
            new_filename = f"decrypted_{filename[len('encrypted_'):]}"
        else:
            new_filename = f"decrypted_{filename}"

    with open(new_filename, 'wb') as f:
        f.write(image_data)

    print(f"✅ {mode.capitalize()}ion complete! Output file: {new_filename}")


# === MAIN PROGRAM ===
import os

# Prompt for user input
image_name = input("📁 Enter image file name (e.g., photo.png): ")
if not os.path.exists(image_name):
    print("❌ File not found. Please make sure the image is in the same folder.")
    exit()

mode = input("🔐 Enter mode (encrypt/decrypt): ").strip().lower()
if mode not in ["encrypt", "decrypt"]:
    print("❌ Invalid mode! Please enter 'encrypt' or 'decrypt'.")
    exit()

key = 45  # You can change this key if you want
encrypt_decrypt_image(image_name, key, mode)