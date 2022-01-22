import sys

dp = [0]*91
def pinary(k):
    if k==1:
        return 1
    if k==2:
        return 1
    if dp[k] != 0:
        return dp[k]
    dp[k] = pinary(k-1) + pinary(k-2)
    return dp[k]

print(pinary(int(sys.stdin.readline())))