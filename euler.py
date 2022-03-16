# Euler's theorem - counts the total number of positive intergers up to n that are co prime with a given number n

# calculate gcd of two #s
def gcd(p, q):
    while q != 0: 
        p, q = q, p%q 
    return p

def is_coPrime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if is_coPrime(x, y)]
        return len(n)

print(phi_func(10))