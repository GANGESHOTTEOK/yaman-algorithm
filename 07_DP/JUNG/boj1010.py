TC = int(input())
dp = [[0 for _ in range(30)] for _ in range(30)]

def combination(n, r):
    if n == r or r == 0:
        return 1

    if r == 1:
        return n

    if dp[n][r]:
        return dp[n][r]
    dp[n][r] = combination(n-1, r) + combination(n-1, r-1)
    return dp[n][r]

while (TC):
    TC -= 1

    N, M = map(int,input().split())
    print(combination(M,N))
