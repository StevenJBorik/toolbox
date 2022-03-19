# If n and k are integers, then n
#                               k
# is the amount of subsets that
# # can be made using k elements 
#in an end set element 'n choose k''

from math import factorial


def chooseCombination(n, k):
    bot = (factorial(n) // factorial(k) * factorial(n - k))
    if bot < 0:
        return None 
    else:
        return bot 

print(chooseCombination(9, 4))