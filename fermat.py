def fermat_little(a):
    if(2**(a - 1) % a) == 1:
         return True
    else: 
        return False

print(fermat_little(67))