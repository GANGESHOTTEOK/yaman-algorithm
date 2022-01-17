from sys import stdin,maxsize

def bellman_ford(start):
    distances = {node:maxsize for node in range(1,n+1)}
    distances[start] = 0
    for i in range(n):
        for cur_node,value in graph.items():
            for next_node,cost in value.items():
                if distances[cur_node] != maxsize and distances[next_node] > distances[cur_node] + cost:
                    distances[next_node] = distances[cur_node] + cost
                    if i == n-1:
                        return True,distances
    distances.pop(1)
    return False,distances


n,m=map(int,stdin.readline().split())
graph = {node:{} for node in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int,stdin.readline().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b],c)
    else:
        graph[a][b] = c

result,ans = bellman_ford(1)
if result:
    print(-1)
else:
    for val in ans.values():
        if val == maxsize:
            print(-1)
        else:
            print(val)