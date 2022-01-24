def max_value(N, P):
    dp = [0 for _ in range(N + 1)]
    dp[1] = P[1]

    for i in range(2, N + 1):
        dp[i] = P[i]
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] + dp[i - j])

    return dp[N]

N = int(input())
P = [0]
P += list(map(int, input().split()))

print(max_value(N, P))