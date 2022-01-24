def tiling(n : int) -> int:
    dp = [0 for _ in range(1001)]
    dp[1], dp[2] = 1, 3

    for i in range(3, n+1):
        dp[i] = ((dp[i - 1] % 10007) + (dp[i - 2] * 2 % 10007)) % 10007

    return dp[n]

n = int(input())
print(tiling(n))