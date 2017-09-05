# pip install pycrypt

from Crypto.PublicKey import RSA
from Crypto import Random

# generate new key
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
public_key = key.publickey()

# encrypt data
enc_data = public_key.encrypt('abcdefgh'.encode('UTF-8'), 32)
# decrypt data
key.decrypt(enc_data)

# export and import key
exportedkey = key.exportKey()
newkey = RSA.importKey(exportedkey)

# export and import key to file
f = open('mykey.pem','w')
var = key.exportKey('PEM')
print(str(var))
f.write(str(var))

print("here")
f.close()
a = open('mykey.pem','r')
#newkey = RSA.importKey(a.read())