import sys
input = sys.stdin.readline

T = [0]*16
P = [0]*16
dp = [0]*16
N = int(input())
for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

for i in range(1,N+1):
    t,p = i+T[i]-1,dp[i]+P[i]
    dp[t] = max(dp[t], p)
    


# print(T, P) 