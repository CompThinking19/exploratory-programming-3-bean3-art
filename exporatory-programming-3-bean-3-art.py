import re
source = open('Pride.txt')
Pride = source.read()
def findat(book):
    if type(book) != str:
        raise TypeError('Not a string')
    result = re.findall('[A-Za-z]+at\\b', book)
    atword = []
    for element in result:
        if len(element) > 3:
            atword.append(element)
    return atword
findat(Pride)
