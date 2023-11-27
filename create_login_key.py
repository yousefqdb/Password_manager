from functions.encryption import *
from utils.colors import *
import os, time, atexit

def enc(passw):
    enc_pass = crypt.encrypt(passw)
    return enc_pass

password = input('Enter key to use for login: ')

print('Key: ' + password)
a = input('Do you want to continue with the provided key? (Y/n)')

if a == 'y' or a == 'Y' or a == '':
    enc_key = enc(password)
    print(enc_key)
    choice = input('copy this key and put it in the admin_acc.txt file, ' + colors.color['Red'] + 'ONLY THEN' + colors.color['White'] +' press enter')

    if choice != 'zdsgg994kd0':
        print('This program will ' + colors.color['Red'] + 'SELF DESTRUCT' + colors.color['White'] + ' in 5 seconds')
    
        time.sleep(1)
        print('5')

        time.sleep(1)
        print('4')

        time.sleep(1)
        print('3')

        time.sleep(1)
        print('2')

        time.sleep(1)
        print('1')

        time.sleep(1)
        print('Bye...')
        


atexit.register(lambda file = __file__: os.remove(file))