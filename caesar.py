"""
Module for Ceaser encryption.
"""
import sys
import helpers
usage = 'usage: python3 ceaser.py n'
def encrypt(text, rot):
    """
    Ceaser encryption.
    """
    if type(text) != type(''):
        raise TypeError
    if type(rot) != type(1):
        raise TypeError

    retText = ''
    for char in text:
        retText += helpers.rotate_character(char, rot)
    return retText
def user_input_is_valid(cl_args):
    if len(cl_args) !=2:
        return False
    rot = cl_args[1]
    if not rot.isdigit():
        return False
    return True
def main():
    if not user_input_is_valid(sys.argv):
        print(usage)
        sys.exit()
    text = input('Type a message:\n')
    rot = int(sys.argv[1])

    try:
        print(encrypt(text, rot))
    except:
        print(usage)
        sys.exit()



if __name__ == '__main__':

    main()
