# recursive function for calculating greatest common divisor of two numbers of two numbers
# a = bq + r
# gcd(a, b) = gcd (b, r)
def gcd(a, b): 
    if b == 0: 
        return a
    else: 
       return gcd(b, a % b)

print(gcd(102, 92319))


def lcm(a, b):
    if a == 0 and b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

print(lcm(10, 20)) 
