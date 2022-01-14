from sys import stdin

n = int(stdin.readline())
if n==1:
    print(1)
else:
    DP = [0]*(n+1)
    DP[1] = 1
    DP[2] = 3
    for i in range(3,n+1):
        DP[i] = DP[i-1] + 2*DP[i-2]
    print(DP[n]%10007)