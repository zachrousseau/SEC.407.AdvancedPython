# Digital signature is a hash signed by the sender's private key.
import rsa
with open('samplePDF.pdf','rb') as f:
    pdf = f.read()

with open('private_key_file.pem','rb') as pr:
    private_key = rsa.PrivateKey.load_pkcs1(pr.read())

signature_file = rsa.sign(pdf,private_key,"SHA-1")

# Print the length of the signatue file which derived from the hash function not the PDF file
print('Digest Size:')
print(len(signature_file))

with open('signature_file','wb') as sf:
    sf.write(signature_file)

