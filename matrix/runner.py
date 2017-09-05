#!/usr/bin/python

import os
import sys
from Matrix import *
from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random
from aes import *
import hashlib


def main():

    options();
    #card = Matrix(1)   
    #print(vars(card))


def options():
    print('___________________________________')
    print('1 - 01')
    print('2 - 02')
    print('3 - ')
    print('4 - ')
    print('5 - Exit')
    print('___________________________________')


if __name__ == '__main__':
    os.system('clear');
    sys.exit(main())
