# find the sequence of fibonacci numbers up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

fib(100000000000000000000000000000000000000000000000000000000000000000000000000)
