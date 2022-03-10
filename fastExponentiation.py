import sys

sys.setrecursionlimit(1500)

def power(a, n): 
    if n == 0: 
        a = 1
    elif n == 1: 
        return a
    else:
        r = power(a, n//2)
        if (n % 2 == 0): 
            return r * r
        else:
            return r * a * r


a = 16
n = 2
print(power(a,n))