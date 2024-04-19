import rsa
with open('samplePDF.pdf','rb') as f: #load the pdf file
    pdf = f.read()

with open('public_key_file.pem','rb') as puk: #load the public key
    public_key = rsa.PublicKey.load_pkcs1(puk.read())

with open('signature_file','rb') as sf:
    signautre_file = sf.read()

verify_file = rsa.verify(pdf, signautre_file,public_key)

# If it is verified then you will get the name of the hash algorithm used.
print('Verify:')
print(verify_file)

#if any change to the pdf file happens, when  you run the code it will give error.

