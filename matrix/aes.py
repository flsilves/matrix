from Crypto.PublicKey import RSA
from Crypto import Random
import json

# generate new key
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)

public_key = key.publickey()

# encrypt data
enc_data = public_key.encrypt('abcdefgh'.encode('UTF-8'), 32)
# decrypt data


print(key.decrypt(enc_data).decode('UTF-8'))

#print(str(enc_data))
# export and import key
#exportedkey = key.exportKey()
#newkey = RSA.importKey(exportedkey)

# export and import key to file
f = open('mykey.pem','wb') # open in byte mode
var = key.exportKey('PEM', 'testes')


f.write(var)


f.close()
a = open('mykey.pem','rb')
newkey2 = RSA.importKey(a.read(), "testes")

public_key = newkey2.publickey()
#print(newkey.exportKey('DER').decode("utf-8"))
enc_data = public_key.encrypt('abcdefgh'.encode('UTF-8'), 32)

print(key.decrypt(enc_data).decode('UTF-8'))


