from cryptography.fernet import Fernet

# usually you read the key from a file
#with open('mykey.key','rb') as key_file:
#    key = key_file.read()
key = b'YCtLIyVrCsv6zQgRIvQ5dMDur4wj27OQlgxe6tj98Y8='

cipher = Fernet(key)


with open('TestFileEncrypted.docx','rb') as f:
    edata = f.read()

edata = cipher.decrypt(edata)  # save your encrypted file

with open('TestFileDecrypted.docx', 'wb') as df:
    df.write(edata)