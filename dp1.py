def combSum(n): 
    dp = [0] * 10 
    dp[0] = 1
    nums = [1, 2, 3]
    for i in range(1, n):
        for x in nums: 
            print(dp[i])
            print('------')
            dp[i] += dp[i - x]
            print(dp[i])
            print('------')

print(combSum(4))