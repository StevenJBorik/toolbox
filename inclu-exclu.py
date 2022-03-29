 
def countDivisors(N, a, b):
 
    # Counts of numbers
    # divisible by a and b
    count1 = N // a
    count2 = N // b
    print(count1)
    print(count2)
 
    # inclusion-exclusion
    # principle applied
    count3 = (N // (a * b))
    print(count3)
 
    return count1 + count2 - count3
 
 
# Driver Code
N = 1000
a = 3
b = 4
print(countDivisors(N, a, b))