from sys import stdin

n,k = map(int, stdin.readline().split())
weight = []
value = []

for _ in range(n):
    w,v = map(int, stdin.readline().split())
    weight.append(w)
    value.append(v)

bag = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i==0 or j==0:
            bag[i][j] = 0
        elif weight[i-1] <= j:
            bag[i][j] = max(value[i-1]+bag[i-1][j-weight[i-1]],bag[i-1][j])
        else:
            bag[i][j] = bag[i-1][j]

print(bag[n][k])