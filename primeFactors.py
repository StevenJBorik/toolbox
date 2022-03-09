# Prime Factors

import math 

# Given n, print all prime factors
def primeFactors(n): 
    while n % 2 == 0:
        print(2) 
        n = n/2
        print(n)
    # n is odd at this point
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            print(i)
            n = n/i 
            print(n)
    if n > 2:
        print(n)  

n = 315
print(primeFactors(n))