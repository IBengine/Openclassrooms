# Code_Cesar_text_file.py
from math import *
import math as mat
import Code_Cesar_CMD as CCC
from sys import argv
from os import getcwd

def ReadFilecwd (text_file_name):
    cwd = getcwd()
    fichier = open(cwd + "\\" + text_file_name + ".txt", "r")
    original_text=fichier.read()
    fichier.close()
    return original_text
    
def CreatFilecwd (text_file_name,text_content):
    cwd = getcwd()
    fichier = open(cwd + "\\" + text_file_name + ".txt", "w")
    original_text=fichier.write(text_content)
    fichier.close()
    return None   
    
def WriteCodecwd (text_file_name):
    cwd = getcwd()
    fichier = open(cwd + "\\" + text_file_name + ".txt", "a")
    original_text=fichier.write("\n"+CCC.CryptageDeCesar(ReadFilecwd(str(argv[1])),int(argv[2])))
    fichier.close()
    return None

if __name__ == '__main__':
    try:
        CreatFilecwd(str(argv[1]),str(argv[3]))
        print CCC.CryptageDeCesar(ReadFilecwd(str(argv[1])),int(argv[2]))
        WriteCodecwd(str(argv[1]))
    except:
        None
