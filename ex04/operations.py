import sys


if (len(sys.argv) < 3):
    print("Usage: python operations.py <number1> <number2> \nExample:\n\
        python operations.py 10 3")
    exit()
if (len(sys.argv) == 3):
    try:
        d = int(sys.argv[1])
        d2 = int(sys.argv[2])
        print("Sum:        ", d + d2)
        print("Difference: ", d - d2)
        print("Product:    ", d * d2)
        if d2 != 0:
            print("Quotient:   ", d / d2)
        else:
            print("Quotient:   ERROR (div by zero)")
        if d2 != 0:
            print("Remainder:  ", d % d2)
        else:
            print("Remainder:  ERROR (modulo by zero)")
    except ValueError:
        print("InputError: only numbers\n\n\
Usage: python operations.py <number1> <number2> \nExample:\n\
        python operations.py 10 3")
else:
    print("InputError: too many arguments")
