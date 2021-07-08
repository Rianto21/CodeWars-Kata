"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

import string #to take the ascii function so we can make list that contain a-z automaticly
def rot13(message):
    am = list(string.ascii_lowercase[0:13]) #a-m list
    nz = list(string.ascii_lowercase[13:26]) #n-z list
    output = '' #to store the letter from for loop
    for i in message: #for every letter in message
        if i.lower() in am: #if i is a-m
            if i.islower(): #if i is lower case
                output += nz[am.index(i.lower())] #output got a new letter in list nz with same index of the letter in list am
            elif i.isupper(): #if i is upper case
                output += nz[am.index(i.lower())].upper() #output got a new letter in list nz with same index of the letter in list am but uppercase
        elif i.lower() in nz: #if i is n-z
            if i.islower(): #if i is lower case
                output += am[nz.index(i.lower())] #output got a new letter in list am with same index of the letter in list nz
            elif i.isupper(): #if i is upper case 
                output += am[nz.index(i.lower())].upper() #output got a new letter in list am with same index of the letter in list am but uppercase
        else: #other than that
            output += i #just put i to output
    return output #return output variable
