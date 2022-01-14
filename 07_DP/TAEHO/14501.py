from sys import stdin

n = int(stdin.readline())
DP = [0]*(n+2)
time = [0]*(n+1)
for i in range(n):
    t, p = map(int,stdin.readline().split())
    time[i+1] = t
    DP[i+1] =p
    DP[i+2] =0

for i in range(n,0,-1):

    if i+time[i] <= n+1:
        DP[i] = max(DP[i]+DP[i+time[i]],DP[i+1])
    else:
        DP[i] = DP[i+1]
    
print(DP[1])

