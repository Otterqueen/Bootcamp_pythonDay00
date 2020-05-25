import sys


def reverse(s):
    return s[::-1]


string = ""
if (len(sys.argv) >= 2):
    for arg in sys.argv[1:]:
        string = string + " " + arg
    string = reverse(string[1:]).swapcase()
    print(string)
