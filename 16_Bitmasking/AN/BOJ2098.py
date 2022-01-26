import sys
input = sys.stdin.readline
INF = sys.maxsize
W = []
N = int(input())
dp = [[None] * (1 << N) for _ in range(N)]
for _ in range(N):
    W.append(list(map(int, input().split())))
    
def TSP(mask, city):
    mask |= (1<<city)
    
    if mask == (1<<N)-1:
        return W[city][0] or INF

    if dp[city][mask] != None:
        return dp[city][mask]
    
    dp[city][mask] = INF
    for i in range(N):
        if i == city:
            continue
        if mask&(1<<i)==0 and W[city][i]>0:
            dp[city][mask] = min(TSP(mask,i)+W[city][i], dp[city][mask])
    return dp[city][mask]

print(TSP(0,0))