from sys import stdin

n = int(stdin.readline())
DP = [[1]*10 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,10):
        DP[i][j] = DP[i][j-1] + DP[i-1][j]

print(DP[i][9]%10007)