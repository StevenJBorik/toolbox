def mod_power(a, n, m):
    r = 1
    while n > 0: 
        if n & n == 1: 
            r = (r * a) % m
        a = (a * a)  % m
        n >>= 1
    return r 



p = 23424024820348209480284028409248029834028340928430928408234082049
print(mod_power(2, p - 1, p))