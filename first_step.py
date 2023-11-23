import getpass
import base64

uname = input("Enter username: ")
p = getpass.getpass(prompt = "Enter your password: ")
creds=uname+"*.*"+p

def encryptcredential(pwd):
  rvalue=base64.b64encode(pwd.encode())
  return rvalue

def decryptcredential(pwd):
    rvalue=base64.b64decode(pwd)
    rvalue=rvalue.decode()
    return rvalue

encryptedcreds=encryptcredential(creds)

print ("Simple creds: {}".format(creds))
print ("Encrypted creds: {}".format(str(encryptedcreds)))
print ("Decrypted creds: {}".format(decryptcredential(encryptedcreds)))
