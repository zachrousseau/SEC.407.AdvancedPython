from cryptography.fernet import Fernet

# usually you read the key from a file
#with open('mykey.key','rb') as key_file:
#    key = key_file.read()

key = b'YCtLIyVrCsv6zQgRIvQ5dMDur4wj27OQlgxe6tj98Y8='

cipher = Fernet(key)

with open('TestFile.docx', 'rb') as f:
    myfile = f.read()

edata = cipher.encrypt(myfile)  # save your encrypted file
with open('TestFileEncrypted.docx', 'wb') as df:
    df.write(edata)

