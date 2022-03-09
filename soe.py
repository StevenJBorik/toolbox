# Sieve of Eratosthenes Aglo
from math import isqrt

def primes_less_than(n: int) -> list[int]:
    # base cases
    # no primes less than 2
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # square of a prime is a composite number w/ 2 factors = sqrt(n)
    # compute until sqrt(n) + 1
    for i in range (2, isqrt(n) + 1):
        if is_prime[i]: 
            # mark multiples of # that are > than
            for x in range(i*i, n, i): 
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]



print(primes_less_than(1000))