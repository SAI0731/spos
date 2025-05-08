import random
from sympy import isprime

# Function to generate a random prime number
def generate_prime(bitsize):
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to generate public and private keys
def generate_keys(bitsize=8):
    p = generate_prime(bitsize)
    q = generate_prime(bitsize)

    # Ensure p and q are distinct
    while p == q:
        q = generate_prime(bitsize)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that e and phi are coprime
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Compute d such that (d * e) % phi = 1
    d = mod_inverse(e, phi)

    # Public key (e, n), Private key (d, n)
    return ((e, n), (d, n))

# Function to encrypt plaintext using the public key
def encrypt(plaintext, pub_key):
    e, n = pub_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

# Function to decrypt ciphertext using the private key
def decrypt(ciphertext, priv_key):
    d, n = priv_key
    decrypted = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted

# Main function to demonstrate RSA
def main():
    # Key Generation
    pub_key, priv_key = generate_keys(bitsize=8)
    print("Public Key: ", pub_key)
    print("Private Key: ", priv_key)

    # Encrypt a message
    plaintext = input("Enter the message to encrypt: ")
    ciphertext = encrypt(plaintext, pub_key)
    print("Ciphertext:", ciphertext)

    # Decrypt the message
    decrypted_message = decrypt(ciphertext, priv_key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
