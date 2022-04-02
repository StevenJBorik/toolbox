

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


# Lucas' theorem is a result about binomial coefficients modulo a prime p.
# We will be given three numbers n, r and p and we need to compute value of nCr mod p.
# Excample 1:
# Q.) : Find the remainder when 1000C300 is divided by 13.
# Sol : First we write 1000 and 300 in terms of the sum of power of 13
#              1000 = 5(13^2) + 11(13) + 12 
#               300 = 1(13^2) + 10(13) + 1
#         Then apply Lucas Theorem:
#                                 1000C300 = (5C1) * (11C10) * (12C1)
#                                          = 5 * 11 * 12
#                                          = 5 *(-2) * (-1) 
#                                          = 10


def dpBinomialC(n, k): 
    dp = [n + 1][k + 1]

    for i in range(0, n - 1): 
        for j in range(0, min(i, k)): 
            if (j == 0 or j == i): 
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + \
                    dp[i - 1][j]
    return dp[n][k]


#Time: O(Pˆ2 + logN)
#Space: O(p)

def nCrModpDP(n, r, p): 
    C = [r + 1]
    C[0] = 1

    for i in range(1, n - 1):
        for j in range(j, min(r, i), -1):
            C[j] = (C[j] + C[j - 1]) % p
    return C[r]




def nCrModPLucas(n, r, p): 
    if r == 0:
        return 1
    ni = n % p
    ri = r % p

    return nCrModPLucas(n / p, r / p, p) *  \
        nCrModpDP(ni, ri, p) % p