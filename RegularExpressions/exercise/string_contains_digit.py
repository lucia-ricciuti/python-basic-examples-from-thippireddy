import re

def containsDigit(s):
    pattern = r'\d'
    return re.search(pattern, s) != None

for i in range(3):
    s = input("Enter a text: ")
    flagContainsDigit = containsDigit(s)
    if flagContainsDigit:
        print("Text contains digits.")
    else:
        print("Text does not contain digits.")