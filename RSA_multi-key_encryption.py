# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import pprint
pp = pprint.PrettyPrinter(depth=25)

def encrypt_function (a,b):
    return (a+1)*b

def decrypt_function (a,b):
    return int((a-1)/b)

pixel_image = []
size=25
for i in range(size):
    
    pixel_image.append(int(random.uniform(0, 255)))
        
print(pixel_image)


matrix_RSA_key = []
for i in range(size):
    
    matrix_RSA_key.append(int(random.uniform(1, 20)))
    
print(matrix_RSA_key)

pixel_image_encrypt = []
for j in range(size):

        pixel_image_encrypt.append(encrypt_function(pixel_image[j], matrix_RSA_key[j]))
    
print(pixel_image_encrypt)


pixel_image_decrypt = []
for j in range(size):

        pixel_image_decrypt.append(decrypt_function(pixel_image_encrypt[j], matrix_RSA_key[j]))
    
print(pixel_image_decrypt)































