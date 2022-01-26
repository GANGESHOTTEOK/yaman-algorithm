from sys import stdin
import heapq as hq

t = int(stdin.readline())
for _ in range(t):
    n,k = map(int,stdin.readline().split())
    time = {node+1: time for node,time in enumerate(map(int,stdin.readline().split()))}
    vertex = {node:0 for node in range(1,n+1)}
    graph = {node:[] for node in range(1,n+1)}
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
        
        for adj_v in graph[v]:
            vertex[adj_v] -= 1
            if vertex[adj_v] == 0:
                hq.heappush(q,(t+time[adj_v], adj_v))
