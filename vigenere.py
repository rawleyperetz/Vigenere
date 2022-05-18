#this is the decryption of Vigenere's Cipher. Damn it, I need to refactor it into a better function
import string 
import numpy as np
import math

#cipherText = input('Enter the cipherText: ')
cipherText = "VPXZGIAXIVWPUBTTMJPWIZITWZT"
key = input('Enter the key: ')

cipher = list(cipherText.lower())
len_cipher = len(cipher)

repeat = key*math.floor(len_cipher/len(key))

if (len_cipher % len(key)) != 0:
    repeat = repeat + key[:(len_cipher % len(key))]

key = list(repeat)

OBA = np.array([cipher, key])

letters = string.ascii_letters[:26]
numbers = range(0,26)
dictionary = { i:letters[i] for i in list(numbers) }

message = [ dictionary[(letters.find(OBA[0][val]) - letters.find(OBA[1][val])) % 26] for val in range(len_cipher)]

print('The message is:', ''.join(message))
