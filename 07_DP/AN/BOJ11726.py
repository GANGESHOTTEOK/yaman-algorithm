import sys

input = sys.stdin.readline
mod = 10007
n = int(input())
dp = [0]*1001

def tile(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if dp[k] != 0:
        return dp[k]
    dp[k] = tile(k-2)+tile(k-1)
    dp[k] %= mod
    return dp[k]
    
print(tile(n))