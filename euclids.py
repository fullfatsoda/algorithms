# Euclid's algorithm to compute the greatest common divisor (GCD) to two numbers
# https://en.wikipedia.org/wiki/Euclidean_algorithm

def get_gcd(a, b):
    while True:
        if b == 0:  # check for 0
            print(a)  # return gcd
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
