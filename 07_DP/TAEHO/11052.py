from sys import stdin

n = int(stdin.readline())
ps = list(map(int,stdin.readline().split()))
DP = [0]*(n+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        DP[i] = max(DP[i],DP[i-j]+ps[j-1])
print(DP[n])