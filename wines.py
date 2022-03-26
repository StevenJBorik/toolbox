# Lines of Wine from Errichto DP Lecture Series

# There are n wines in a row, each year you sell either the 
# leftmost or the rightmost wine. The ith wine has initial
# price p[i] and price k * p[i] in the kth year.
# What is the maximum total profit?



N = 1000

#store of state
dp = [[-1 for r in range(N)]
          for c in range(N)]
# store of strategy
sell = [[0 for a in range(N)]
           for b in range(N)]


def maxProfitCalc(price, begin, end, n):
    
    if (dp[begin][end] != -1):
        return dp[begin][end]


    year = n - (end - begin)
    
    # states have reached equivalent points in array 
    if (begin == end):
        return year * price[begin]

    # x = maximum profit on selling the
    # wine from the front this year
    x = price[begin] * year + maxProfitCalc(price, begin + 1, end, n)
 
    # y = maximum profit on selling the
    # wine from the end this year
    y = price[end] * year + maxProfitCalc(price, begin, end - 1, n)
    
    ans = max(x, y)
    dp[begin][end] = ans

    if (x >= y):
        sell[begin][end] = 0
    else:
        sell[begin][end] = 1
 
    return ans

def maxProfit(price, n):
    # price, beginning, ending, n
    ans = maxProfitCalc(price, 0, n - 1, n)
    
    i = 0
    j = n - 1

    while (i <= j):
        if (sell[i][j] == 0):
            i += 1
        else:
            j -= 1
    return ans

price = [2, 4, 6, 2, 5]
size = 5

ans = maxProfit(price, size)
print(ans)
 