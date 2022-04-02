

import math

def nCr(n,r):
    f = math.factorial
    print(f(n))
    print(f(r))
    print(f(n-r))
    return f(n) / f(r) / f(n-r)
# print(nCr(4, 2))

def binCoRecurs(n, k):
    if k == 0 or n == k:
        return 1
    return binCoRecurs(n - 1, k -1) + \
    binCoRecurs(n - 1, k)

print(binCoRecurs(2, 1))

