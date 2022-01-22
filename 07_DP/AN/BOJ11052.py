import sys
input = sys.stdin.readline

dp = [0]*1001
P = [0]*1001
N = int(input())
P[1:N+1] = list(map(int, input().split()))
dp[1] = P[1]
for i in range(2,N+1):
    M = 0
    for k in range(1,i+1):
        M = max(M,dp[k]+dp[i-k])
    dp[i] = max(M,P[i])

print(dp[N])