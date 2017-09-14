from Keyhandler import *
import os

def display_options():
    print('___________________________________')
    print('1 - Import Key')
    print('2 - Export Key')
    print('3 - Encode')
    print('4 - Decode')
    print('5 - Exit')
    print('___________________________________')

def Menu():
    kh = Keyhandler()    ## TODO use enum

    while True:
        display_options()
        value = input("Make a selection> ")
        if '1' in value:
            kh.import_key()
        elif '2' in value:
            kh.create_key()
        elif '3' in value:
            encoded = kh.encode('text')
        elif '4' in value:
            kh.decode(encoded)
        elif '5' in value:
            print('Good-bye')
            quit()
        else:
            print('Invalid menu choice.')

if __name__ == '__main__':
    Menu()