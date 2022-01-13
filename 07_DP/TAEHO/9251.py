from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
l1 = len(s1)
l2 = len(s2)
DP = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1] == s2[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i][j-1],DP[i-1][j])

print(DP[l1][l2])