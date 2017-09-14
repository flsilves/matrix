from Crypto.PublicKey import RSA
from Crypto import Random
from os import path
from getpass import getpass

class Keyhandler:

    def __init__(self):
        self.random_generator =  Random.new().read
        self.key = RSA.generate(2048, self.random_generator)

    def import_key(self):
        self.key_file = input('>>Enter key filename: ')
        if(path.isfile(self.key_file)):
            print('Imported key: {0}'.format(self.key_file))
        else:
            print('File does not exist {0}'.format(self.key_file))
            quit(0)
        passphrase = getpass('>> Enter passphrase: ')
        handler = open(self.key_file, 'rb')
        self.key = RSA.importKey(handler.read(), passphrase)
        print('Key imported sucessfully')

    def create_key(self):
        self.exported_file = input('>> Enter filename to create new key: ') ## check file extension and add accordingly
        passphrase = getpass('>> Enter passphrase: ')
        fileHandler = open(self.exported_file,'wb') ## open in byte mode
        fileHandler.write(self.key.exportKey('PEM', passphrase))
        print('Key \"{0}\" created successfully.'.format(self.exported_file))

    def encode(self, input_text):
        print(input_text)
        print(input_text.encode('UTF-8'))
        self.public_key = self.key.publickey()
        enc_data = self.public_key.encrypt(input_text.encode('UTF-8'), 32)
        return enc_data

    def decode(self, input_text):
        decoded = self.key.decrypt(input_text)
        print(decoded.decode('UTF-8'))

