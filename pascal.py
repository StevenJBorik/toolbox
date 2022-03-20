
hash =  {}
def pascal(row, col):
    index = (row,col)
    if index in hash: return hash[index]
    if (col == 1):
        return 1
    if (col == row):
        return 1
    
    upLeft = pascal(row - 1, col - 1)
    upRight = pascal(row - 1 , col)
    hash[index] = upLeft + upRight
    return upLeft + upRight 

for r in range(1, 10):
    for c in range (1, r  + 1): 
        print(pascal(r,c), end = " ")
    print("")

pascal 