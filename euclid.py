# recursive function for calculating greatest common divisor of two numbers of two numbers
# always getting remainder of larger number in recursive funciton call 
# a = bq + r
# gcd(a, b) = gcd (b, r)

def gcd(a, b): 
    if b == 0: 
        return a
    else: 
       print(a, b)
       return gcd(b, a % b)

print(gcd(1000, 100000))


def lcm(a, b):
    if a == 0 and b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def xgcd(a, b):
    if b == 0: 
        d, x, y = a, 1, 0
        return d, x, y
    else:
        d, x1, y1 = xgcd(b, a % b)
        q = a // b
        x1 = y1
        y1 = x1 - y1*q
        return d, x, y   



print(lcm(10, 20)) 
