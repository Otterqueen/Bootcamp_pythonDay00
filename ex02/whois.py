import sys


if len(sys.argv) != 2:
    print("ERROR")
    exit()
else:
    try:
        d = int(sys.argv[1])
    except ValueError:
        print("ERROR")
        exit()
    if d == 0:
        print("I'm Zero.")
    elif (d % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
