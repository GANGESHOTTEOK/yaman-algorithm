def tiling(n):
    dp = [0] * 1001
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] % 10007 + dp[i-2] % 10007) % 10007

    return dp[n]


n = int(input())
print(tiling(n))