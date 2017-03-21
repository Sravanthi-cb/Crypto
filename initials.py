
def get_initials(fullName):
    if type(fullName) != type(''):
        raise TypeError
    words = fullName.split()
    initials = ''
    for word in words:
        word = word.strip()
        if len(word) >= 1:
            initials += word[0].upper()
    return initials
def main():

    name = input('What is your full name?\n')
    initials = get_initials(name)
    print(initials)
    

if __name__ == '__main__':
    main()
