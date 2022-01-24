def pinary_number(N):
    dp = [0] * 100
    dp[1], dp[2] = 1, 1

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[N]

N = int(input())
print(pinary_number(N))