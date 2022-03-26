# import sys

# sys.setrecursionlimit(10000)

# def power(a, b):
#     if b == 0:
#         return 1
#     tmp = power(a, b / 2)
#     result = tmp * tmp
#     if b % 2 == 1:
#         result *= a
#     return result

# print(power(3, 5))

def powerIterative(a, b):
    result = 1
    while b:
        if b % 2 == 1: result *= a
        a *= a
        b /= 2
    return result 

print(powerIterative(3, 3))


