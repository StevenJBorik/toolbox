def catalanNums(n):
    if n <= 1:
        return 1
    
    res_n = 0
    for i in range(n):
        res_n += catalanNums(i) * catalanNums(n - i - 1) 
    return res_n

print(catalanNums(5))
