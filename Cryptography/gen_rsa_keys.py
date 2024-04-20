# https://stuvel.eu/python-rsa-doc/
import rsa

# generating two keys
shakour_pub, shakour_priv = rsa.newkeys(1024)

# printing the private key
print(shakour_priv.save_pkcs1('PEM').decode())

# printing the public key
print(shakour_pub.save_pkcs1('PEM').decode())

# ecryptet data
e_data = rsa.encrypt(b'this is my secret message', shakour_pub)

# printing the encrypted data
print("\nEncrypted MSG:")
print(e_data)

# decrypt data
d_data = rsa.decrypt(e_data,shakour_priv)

# priting the decrypted data
print("\nDecrypted MSG:")
print(d_data.decode())

