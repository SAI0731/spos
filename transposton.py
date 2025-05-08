# Function to perform encryption using the columnar transposition cipher
def encrypt(message, key):
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Create a matrix for the message with rows equal to the key length
    grid = []
    for i in range(len(message) // key + (1 if len(message) % key != 0 else 0)):
        grid.append(list(message[i * key: (i + 1) * key]))

    # If the last row is smaller, pad it with extra spaces
    while len(grid[-1]) < key:
        grid[-1].append(' ')

    # Read the grid column by column
    ciphertext = ""
    for col in range(key):
        for row in grid:
            ciphertext += row[col]
    
    return ciphertext

# Function to perform decryption using the columnar transposition cipher
def decrypt(ciphertext, key):
    # Calculate the number of rows
    num_rows = len(ciphertext) // key
    num_extra = len(ciphertext) % key

    # Create the grid and fill it column by column
    grid = [[''] * num_rows for _ in range(key)]

    idx = 0
    for col in range(key):
        for row in range(num_rows):
            if idx < len(ciphertext):
                grid[col][row] = ciphertext[idx]
                idx += 1

    # Read the grid row by row to get the plaintext
    plaintext = ""
    for row in range(num_rows):
        for col in range(key):
            if grid[col][row] != ' ':
                plaintext += grid[col][row]
    
    return plaintext

# Example usage
message = input("Enter the message to be encrypted: ")
key = int(input("Enter the key (column size): "))

# Perform encryption
encrypted_message = encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

# Perform decryption
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
