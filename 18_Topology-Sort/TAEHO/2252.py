from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())
vertex = {node:0 for node in range(1,n+1)}
graph = {node:{} for node in range(1,n+1)}
visit = {node:0 for node in range(1,n+1)}
answer = []
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a][b] = 1
    vertex[b] += 1

q= deque()
for i in range(1,n+1):
    if vertex[i] == 0 and visit[i] == 0:
        q.append(i)
        print(i,end=" ")
        while q:
            v = q.popleft()
            
            for adj_v in graph[v].keys():
                vertex[adj_v] -= 1
                if vertex[adj_v] == 0:
                    q.append(adj_v)
                    print(adj_v,end=" ")
                    visit[adj_v] = 1

