"""
Module for Ceaser encryption.
"""
import sys
import helpers
usage = 'usage: python3 ceaser.py n'
def encrypt(text, key):
    """
    Ceaser encryption.
    """

    if type(text) != type(''):
        raise TypeError
    if type(key) != type(''):
        raise TypeError
    if not key.isalpha():
        raise TypeError
        
    retText = ''
    index = 0
    keySize = len(key)
    for char in text:
        if char.isalpha():
            kchar = key[index]
            index += 1
            index = index % keySize
            rot = helpers.alphabet_position(kchar)
            retText += helpers.rotate_character(char, rot)
        else:
            retText += char
            
    return retText

def main():
    if len(sys.argv) != 2:
        print( usage)
        sys.exit()
    text = input('Type a message:\n')
    key = sys.argv[1]
    key = key.strip()

    try:
        print(encrypt(text, key))
    except TypeError:
        print(usage)
        sys.exit()
    
        
        
if __name__ == '__main__':

    main()
