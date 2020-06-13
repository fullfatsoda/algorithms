# Euclid's algorithm to compute the greatest common divisor (GCD) to two numbers
# run from command line with...
    #... > python3 euclids.py a b
# where a and b would be two integers e.g. 3050 5060
import sys

def get_gcd(a, b):

    while True:
        if b == 0: # check for 0
            print(a) # return gcd
            return False
        elif a > b:
            a = (a - b)
            print(f"{a} {b}")
            continue
        elif a == 0:
            print(b)
            return False
        else:
            b = (b - a)
            print(f"{a} {b}")
            continue

get_gcd(int(sys.argv[1]), int(sys.argv[2]))
