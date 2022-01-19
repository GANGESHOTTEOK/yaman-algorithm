from sys import stdin,maxsize
import heapq as hq
INF = maxsize
n = int(stdin.readline())
m = int(stdin.readline())

#------------------Floyd-Warshall-------------------#
def Floyd():
    graph = [[0]*n for _ in range(n)]

    for _ in range(m):
        a,b,c = map(int,stdin.readline().split())
        if graph[a-1][b-1]:
            graph[a-1][b-1] = min(graph[a-1][b-1],c)
        else:
            graph[a-1][b-1] = c

    for i in range(n):
        for j in range(n):
            if i==j:
                graph[i][j] = 0
            elif graph[i][j] == 0:
                graph[i][j] = INF

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

    for i in range(n):
        for j in range(n):
            print(0 if graph[i][j] == INF else graph[i][j],end=" ")
        print()

#------------------Dijacstra-------------------#
def Dijacstra():
    graph = {node: {} for node in range(1,n+1)}
    for _ in range(m):
        a,b,c = map(int,stdin.readline().split())
        if b in graph[a]:
            graph[a][b] = min(graph[a][b],c)
        else:
            graph[a][b] = c
    

    for i in range(1,n+1):
        distances = {node:INF for node in range(1,n+1)}
        distances[i] = 0
        q = []
        hq.heappush(q,(distances[i],i))
        while q:
            cur_dist, node = hq.heappop(q)
            if cur_dist > distances[node]:
                continue

            for adj_node,distance in graph[node].items():
                w_dist = distance + cur_dist
                if w_dist < distances[adj_node]:
                    distances[adj_node] = w_dist
                    hq.heappush(q,(w_dist,adj_node))
        
        for val in distances.values():
            print(0 if val==INF else val,end=" ")
        print()

# Floyd()
Dijacstra()