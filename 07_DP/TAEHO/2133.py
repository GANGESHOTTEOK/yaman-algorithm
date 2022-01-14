from sys import stdin

n = int(stdin.readline())
if n==1:
    print(0)
else:
    DP = [0]*(n+1)
    DP[0] = 1
    for i in range(2,n+1,2):
        DP[i] = DP[i-2]*3 
        for j in range(i-4,-1,-2):
            DP[i] += 2*DP[j]
    print(DP[n])