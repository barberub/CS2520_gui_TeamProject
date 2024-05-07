# Author: Leonardo Davalos

import random
import base64


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0 = m
    x0 = 0
    x1 = 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def is_prime(n, k=5):
	"""
    Check if a given number is prime using the Miller-Rabin primality test.

	Args:
		n (int): The number to check for primality.
        k (int): The number of iterations for the Miller-Rabin test. Higher values of k
                 provide higher probability of correctness at the expense of performance.
                 Default is 5.

	Returns:
		bool: True if the number is prime, False otherwise.
	"""
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0:
		return False
	else:
		d = n - 1
		while d % 2 == 0:
			d //= 2
        # Perform Miller-Rabin test k times
		for _ in range(k):
			a = random.randint(2, n - 2)
			x = pow(a, d, n)
			if x == 1 or x == n - 1:
				continue
			for _ in range(n.bit_length() - 1):
				x = pow(x, 2, n)
				if x == n - 1:
					break
			else:
				return False
	return True


def is_prime(n):
    """
    Check if a given number is prime using trial division.
    
    Parameters:
        n (int): The number to check for primality.
                 
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime(length):
    while True:
        p = generate_prime_candidate(length)
        if is_prime(p):
            return p


def generate_key_pair():
    # Choose prime numbers p and q
    p = generate_prime(10)
    q = generate_prime(10)

    # Compute n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi)

    # Return public and private keys
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


def encrypt(message, public_key):
	e, n = public_key
	cipher = [pow(ord(char), e, n) for char in message]
 
	print("Cipher", cipher)
    
    # Convert the list of integers to bytes
	binary_strings = [format(num, '032b') for num in cipher]
    
	#print("Cipher", binary_strings)

	# Concatenate binary strings
	binary_concatenated = ''.join(binary_strings)

	# Convert binary string to bytes
	byte_array = int(binary_concatenated, 2).to_bytes((len(binary_concatenated) + 7) // 8, byteorder='big')

    # Encode the cipher bytes to base64
	encoded_cipher = base64.b64encode(byte_array)
	
	return encoded_cipher


def decrypt(encoded_cipher, private_key):
	d, n = private_key
 
    # Decode the base64-encoded cipher
	cipher_bytes = base64.b64decode(encoded_cipher)
 
    # Convert bytes to binary string
	binary_concatenated = ''.join(format(byte, '08b') for byte in cipher_bytes)

	# Split the binary string into binary strings for each integer
	binary_strings = [binary_concatenated[i:i+32] for i in range(0, len(binary_concatenated), 32)]

	#print("Cipher", binary_strings)

	# Convert binary strings to integers
	cipher = [int(binary, 2) for binary in binary_strings]

	print("Cipher", cipher)

	# Decrypt
	message = ''.join([chr(pow(char, d, n)) for char in cipher])
	return message


def main():
    # Generate key pair
	public_key, private_key = generate_key_pair()

	# Print keys
	print("Public Key (e, n):", public_key)
	print("Private Key (d, n):", private_key)

	# Plain text message
	plain_text = "Hello, World!"

	# Encrypting the message with the public key
	cipher_text = encrypt(plain_text, public_key)
	print("Cipher text:", cipher_text)

	# Decrypting the cipher text with the private key
	decrypted_text = decrypt(cipher_text, private_key)
	print("Decrypted text:", decrypted_text)
 
 
if __name__ == "__main__":
    main()