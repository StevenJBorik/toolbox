# You are given 𝑁≤20 numbers, each up to 10ˆ9. Is there a subset with sum equal to given goal 𝑆?

# with different values of x, we'll get different sets
# Solution iterate over every number 𝑥 from 0 to (2ˆ𝑛)−1 <-- number of possible subsets  
# and considers 𝑥 to be a binary number of length 𝑛, where bit 1 means taking a number and bit 0 is not taking.
# 0 2ˆn x n
    # 2^n = number of subsets x n - all bits in se t 
def subsetSum(n):
     a = []
     S = 20 
     mask = 0 
     for mask in range(0, mask < (1 << n)): 
         sum_of_this_subset = 0
         i = 0 
         for i in range(0, i < n): 
             if (mask & (1 << i)):
                 sum_of_this_subset += a[i]
                 print(a[i])
         if (sum_of_this_subset == S): 
                print('Yes')
                return 0
     print('No')

subsetSum(10)

