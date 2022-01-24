n, k = map(int, input().split())
coins = [0]
for _ in range(n):
    coins.append(int(input()))

dp = [0] * 10001
for coin in coins:
    for j in range(1, k+1):
        if j == coin:
            dp[j] = dp[j] + 1
        elif j > coin:
            dp[j] = dp[j] + dp[j - coin]

print(dp[k])