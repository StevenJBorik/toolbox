from random import randint, random

p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(p)
def shuffle(p, n):
    for i in range(n):
        j = randint(0,i)
        p[i], p[j] = p[j], p[i]
print(shuffle(p, n))