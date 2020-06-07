# Code_Cesar_CMD.py
from math import *
import math as mat
from sys import argv
# original_text = "Ave Caesar morituri te salutant"

def CryptageDeCesar (original_text,shifting_number):
    ordzmin=ord('z')
    ordzmaj=ord('Z')
    Number_character_alphabet=int(ordzmin-ord('a'))+1
    shifting_number=abs(int(shifting_number))
    while shifting_number > Number_character_alphabet:
        shifting_number=shifting_number-Number_character_alphabet
    new_text = ''
    for i in range(int(len(original_text))):
        current_character=original_text[i]
        # if current_character == "_" :
            # new_character = " "
        if not ((ord(current_character)>= ord('a') and ord(current_character)<= ordzmin) or (ord(current_character)>= ord('A') and ord(current_character)<= ordzmaj)):
            new_character=current_character
        else:
            if ord(current_character) > int(ordzmaj):
                Limit_alphabet = int(ordzmin) #minuscule
            else:
                Limit_alphabet = int(ordzmaj) #MAJUSCULE
            new_character=chr(ord(current_character)+shifting_number)
            if ord(new_character) > Limit_alphabet:
                new_character=chr(ord(new_character)-Number_character_alphabet)
        new_text=new_text+new_character
    return new_text
    
if __name__ == '__main__':
    try:
        print(CryptageDeCesar(str(argv[1]),int(argv[2])))
    except:
        None
