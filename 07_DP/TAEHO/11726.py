from sys import stdin

n = int(stdin.readline())

DP = [0]*(n+1)
if n == 1:
    print(1)
else:
    DP[1] = 1
    DP[2] = 2

    for i in range(3,n+1):
        DP[i] = DP[i-1] + DP[i-2]

    print(DP[n]%10007)