import rsa

message = b' this is our text to hash'

htext = rsa.compute_hash(message,'SHA-512')

# print the digest in hexidecimal format
print("Digest:")
print(htext.hex())
print()

# changing one letter in the message
message = b' This is our text to hash'

htext = rsa.compute_hash(message,'SHA-512')
print("Digest with One Letter Change in the Message:")
print(htext.hex())
print()

