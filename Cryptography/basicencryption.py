# Library: https://pypi.org/project/cryptography/
from cryptography.fernet import Fernet

key = Fernet.generate_key() # generate the key
print("KEY:\n",key)

cipher = Fernet(key) # incorporate the key with the cipher

# Bytes literals are utilized for representing binary data like encoded text, pictures, audio, or any other type of data
# that may not directly correspond to characters.
encrypted_text = cipher.encrypt(b'this is my secret') # encrypt the string

print("Encrypted Text:\n", encrypted_text)


decrypted_text = cipher.decrypt(encrypted_text)

print("Decrypted Text\n",decrypted_text.decode())

