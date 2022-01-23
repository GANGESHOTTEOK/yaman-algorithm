import sys

input = sys.stdin.readline
dp = [0]*11

def makeSum(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    if dp[k]!=0:
        return dp[k]
    dp[k] = makeSum(k-1) + makeSum(k-2) + makeSum(k-3)
    return dp[k]

T = int(input())

for _ in range(T):
    n = int(input())
    print(makeSum(n))