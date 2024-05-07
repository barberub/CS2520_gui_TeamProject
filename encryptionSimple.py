# Authors: Leonardo Davalos, Ruben Barbero

# Shift Cipher
def caesar_cipher(text, shift):
	encrypted_text = ''
	for char in text:
		
		#Skip non-alphabet Chars
		if( not char.isalpha() ):
			encrypted_text += char
			continue

		shifted = ord(char) + shift
  
		if char.islower():
			
			if shifted > ord('z'):
				shifted -= 26
			elif shifted < ord('a'):
				shifted += 26
    
		elif char.isupper():

			if shifted > ord('Z'):
				shifted -= 26
			elif shifted < ord('A'):
				shifted += 26
		
		encrypted_text += chr(shifted)
        
	return encrypted_text

# Letter Subsitution
def substitution_cipher(text, key):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	encrypted_text = ''
	for char in text:
		
		#Skip non-Alpha
		if (not char.isalpha()):
			encrypted_text += char
			continue
			
		#Keep Case In Messages
		if char.islower():
			encrypted_text += key[alphabet.index(char)]
		elif char.isupper():
			encrypted_text += key[alphabet.index(char.lower())].upper()
        
	return encrypted_text

# Letter Subsitution
def substitution_decrypt(text, key):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	plain_text = ''
	for char in text:
		
		#Skip non-Alpha
		if (not char.isalpha()):
			plain_text += char
			continue
			
		#Keep Case In Messages
		if char.islower():
			plain_text += alphabet[key.index(char)]
		elif char.isupper():
			plain_text += alphabet[key.index(char.lower())].upper()
        
	return plain_text

def vigenere_encrypt(text, key):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	key_index = 0
	encrypted_text = ""
	for char in text:

		#Skip non-Alpha
		if (not char.isalpha()):
			encrypted_text += char
			continue
		# Number to shift by 
		shift_amount = alphabet.index(key[key_index]) + 1

		# Keep Case in Messages (%len(alphabet) to wrap around if necessary.)
		if char.islower():
			encrypted_text += alphabet[(alphabet.index(char) + shift_amount)%(len(alphabet))]
		elif char.isupper():
			encrypted_text += alphabet[(alphabet.index(char.lower()) + shift_amount)%(len(alphabet))].upper()
		
		# increment key_index, wrapping around to 0 if necessary.
		key_index = (key_index + 1)%len(key)
	
	return encrypted_text

# Differs from encrypt by shifting backwards instead.
def vigenere_decrypt(text, key):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	key_index = 0
	encrypted_text = ""
	for char in text:

		#Skip non-Alpha
		if (not char.isalpha()):
			encrypted_text += char
			continue
		# Number to shift by 
		shift_amount = alphabet.index(key[key_index]) + 1

		# Keep Case in Messages (%len(alphabet) to wrap around if necessary.)
		if char.islower():
			encrypted_text += alphabet[(alphabet.index(char) - shift_amount)%(len(alphabet))]
		elif char.isupper():
			encrypted_text += alphabet[(alphabet.index(char.lower()) - shift_amount)%(len(alphabet))].upper()
		
		# increment key_index, wrapping around to 0 if necessary.
		key_index = (key_index + 1)%len(key)
	
	return encrypted_text

def CaesarMain():
	text = "Hello, World!"
 
	encrypted_text = caesar_cipher(text, 1)
	print("Caesar Encrypted:", encrypted_text)
	print("Caesar decrypted:", caesar_cipher(encrypted_text, -1))


def SubstitutionMain():
    #Key needs to be a length 26 string of chars
	substitution_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
	text = "Hello, World!"
 
	encrypted_text = substitution_cipher(text, substitution_alphabet)
	print("Substitution Encrypted:", encrypted_text)
	print("Back to regular", substitution_decrypt(encrypted_text, substitution_alphabet))

def VigenereMain():
	text = "Hello, World!"
	key = "key"
 
	encrypted_text = vigenere_encrypt(text, key)
	print("vigenere Encrypted:", encrypted_text)
	print("vigenere decrypted:", vigenere_decrypt(encrypted_text, key))



def main():
	CaesarMain()
	SubstitutionMain()
	VigenereMain()
	return
	
 
if __name__ == "__main__":
    main()