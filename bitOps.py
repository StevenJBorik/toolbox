# prints the indices of bits where there is one in number x
def bitOps(x): 
    for i in range(0, 30): 
        if (x & (1 << i)) != 0:
            print(1)
        else:
            print(0)
        
bitOps(93)