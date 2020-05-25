import sys
import string


def is_ponctuation(s):
    if s in string.punctuation:
        return True
    else:
        return False


def text_analyzer(*text):
    """This function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text."""
    if (len(text) != 1):
        print("ERROR")
        return
    elif len(text) == 0:
        text = input("What is the text to analyse?\n")
    else:
        text = text[0]
        if text == "":
            print("ERROR")
            return
    print("The text contains ", len(text), " characters:\n")
    print("- ", sum(map(str.isupper, text)), " upper letters\n")
    print("- ", sum(map(str.islower, text)), " lower letters\n")
    print("- ", sum(map(is_ponctuation, text)), " punctuation marks\n")
    print("- ", sum(map(str.isspace, text)), " spaces")
