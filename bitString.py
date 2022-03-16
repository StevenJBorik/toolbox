from ast import BitAnd


def bitString(n):
    #2^n
    mod = 10**9 + 7
    n = 2**n % mod
    print(n)

bitString(3)
