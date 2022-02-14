from sys import stdin
import heapq as hq
from collections import deque


# 최소 힙 사용
t = int(stdin.readline())
for _ in range(t):
    n,k = map(int,stdin.readline().split())
    time = [0, *map(int,stdin.readline().split())]
    vertex = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x,y = map(int,stdin.readline().split())
        graph[x].append(y)
        vertex[y] += 1

    target = int(stdin.readline())
    q = []
    
    for i in range(1,n+1):
        if vertex[i] == 0:
            hq.heappush(q,(time[i],i))
            
    while q:
        t,v = hq.heappop(q)
        
        if v == target:
            print(t)
            break
        
        for adj_v in graph[v]:
            vertex[adj_v] -= 1
            if vertex[adj_v] == 0:
                hq.heappush(q,(t+time[adj_v], adj_v))

# DP 사용
# t = int(stdin.readline())

# for _ in range(t):
#     n,k = map(int, stdin.readline().split())
#     time = [0] + list(map(int,stdin.readline().split()))
#     graph = {node:[] for node in range(1,n+1)}
#     indegree = {node:0 for node in range(1,n+1)}
#     DP = [0]*(n+1)
#     q = deque()

#     for _ in range(k):
#         x,y = map(int, stdin.readline().split())
#         graph[x].append(y)
#         indegree[y] += 1

#     target = int(stdin.readline())
#     for i in range(1,n+1):
#         if indegree[i] == 0:
#             DP[i] = time[i]
#             q.append(i)
    
#     while q:
#         build = q.popleft()
#         for node in graph[build]:
#             indegree[node] -= 1
#             DP[node] = max(DP[build]+time[node],DP[node])
#             if indegree[node] == 0:
#                 q.append(node)
    
#     print(DP[target])
