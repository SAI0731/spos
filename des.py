from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

# Function to pad the input text to make it a multiple of 8 bytes (64-bits)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '  # Adding space to the text to make it multiple of 8 bytes
    return text

# Function to encrypt using DES
def encrypt_DES(key, plaintext):
    # Ensure the plaintext is padded to be a multiple of 8 bytes
    plaintext = pad(plaintext)

    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return binascii.hexlify(ciphertext).decode('utf-8')

# Function to decrypt using DES
def decrypt_DES(key, ciphertext):
    # Convert the ciphertext back from hex to bytes
    ciphertext = binascii.unhexlify(ciphertext)

    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(ciphertext).decode('utf-8').strip()
    return decrypted_text

# Main function
def main():
    # Sample key (must be 8 bytes long)
    key = b'12345678'  # 8-byte key for DES encryption

    # Sample plaintext
    plaintext = "Hello, this is DES encryption example!"

    # Encrypt the plaintext
    print(f"Original plaintext: {plaintext}")
    encrypted = encrypt_DES(key, plaintext)
    print(f"Encrypted (Hex format): {encrypted}")

    # Decrypt the ciphertext
    decrypted = decrypt_DES(key, encrypted)
    print(f"Decrypted text: {decrypted}")

# Run the program
if __name__ == "__main__":
    main()
