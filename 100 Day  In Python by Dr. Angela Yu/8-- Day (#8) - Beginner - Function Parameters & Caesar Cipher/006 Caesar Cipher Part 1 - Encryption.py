# 006 Caesar Cipher Part 1 - Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt. type 'decode' to decrypt   ..\n")

text = input("Type your message :\n").lower()
shift = int(input("Type the shift Number : \n  "))
"""
Creating a function to define our parameters 
"""

def encrypt(plainT, shiftAmount):
    Cipher_Text = ""
    for letter in plainT:
        position = alphabet.index(letter)
        new_position = position + shiftAmount
        new_letter = alphabet[new_position]
        Cipher_Text += new_letter
    print(f"This code text is {Cipher_Text}")


encrypt(plainT=text, shiftAmount=shift)



