from sys import stdin,maxsize,setrecursionlimit
setrecursionlimit(int(1e6))

def dfs(idx,visit):
    if DP[idx][visit]:
        return DP[idx][visit]

    if visit == (1<<n)-1:
        if graph[idx][0]:
            return graph[idx][0]
        else:
            return maxsize
    
    cost = maxsize
    for i in range(1,n):
        if (visit & (1<<i))==0 and graph[idx][i]:
            cost = min(cost,dfs(i,visit|1<<i) + graph[idx][i])

    DP[idx][visit] = cost
    return DP[idx][visit]

n = int(stdin.readline())
graph = []
DP = [[0]*(1<<n) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,stdin.readline().split())))

print(dfs(0,1))