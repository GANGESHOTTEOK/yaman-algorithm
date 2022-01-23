import sys

input = sys.stdin.readline

dp = [[0 for i in range(30)] for j in range(30)]
def binomial(n,k):
    if n==k or k==0:
        return 1
    if dp[n][k] != 0:
        return dp[n][k]
    dp[n][k] = binomial(n-1,k-1)+binomial(n-1,k)
    return dp[n][k]

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    print(binomial(M,N))