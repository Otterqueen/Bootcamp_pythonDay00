import sys
import string

if (len(sys.argv) != 3):
    print("ERROR")
    sys.exit()

if sys.argv[1].isdigit():
    print("ERROR")
    sys.exit()
else:
    mystr = sys.argv[1]

if sys.argv[2].isdigit():
    len_min = int(sys.argv[2])
else:
    print("ERROR")
    sys.exit()

mystr = mystr.translate(str.maketrans('', '', string.punctuation))
mylist = mystr.split(" ")
i = 0
while i < len(mylist):
    if len(mylist[i]) <= len_min:
        del(mylist[i])
    else:
        i = i + 1
print(mylist)
