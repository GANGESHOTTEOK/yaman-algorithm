from sys import stdin

n,k = map(int,stdin.readline().split())
coins = []
DP = [0]*(k+1)
for _ in range(n):
    coin = int(stdin.readline())
    coins.append(coin)

DP[0] = 1
for coin in coins:
    for i in range(1,k+1):
        if i >= coin:
            DP[i] += DP[i-coin]

print(DP[k])
        
