import sys
sys.setrecursionlimit(10**6)

dp = [0]*1001
def tiles(k):
    if k==1:
        return 1
    if k==2:
        return 3
    if dp[k] != 0:
        return dp[k]
    dp[k] = tiles(k-1) + tiles(k-2)*2
    dp[k] %= 10007
    return dp[k]

print(tiles(int(sys.stdin.readline())))