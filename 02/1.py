import sys

def saberi(a, b):
    return a+b

try:
    a = int(input("a: "))
    b = int(input("b: "))

    print(saberi(a, b))
except:
    sys.exit("ovo nisu brojevi!!!")
