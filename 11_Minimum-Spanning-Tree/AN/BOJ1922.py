import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [] # (cost, start, end)
ex = [i for i in range(0,N+1)]
min_val = 0

def find(u):
    if u == ex[u]:
        return u
    ex[u] = find(ex[u])
    return ex[u]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    
    if root1 > root2:
        ex[root2] = root1
    else:
        ex[root1] = root2

for _ in range(M):
    A,B,C = map(int, input().split())
    edges.append((C,A,B))

edges.sort()

for cost,start,end in edges:
    if find(start) != find(end):
        union(start, end)
        min_val += cost
    
print(min_val)

# prim algorithm
# import sys
# from collections import defaultdict

# input = sys.stdin.readline
# INF = sys.maxsize

# N = int(input())
# M = int(input())

# edges = {i: [] for i in range(1,N+1)}
# dist = [INF]*(N+1)
# visited = [0]*(N+1)

# for _ in range(M):
#     a,b,c = map(int, input().rstrip().split())
#     edges[a].append((c,b))
#     edges[b].append((c,a))
    
# # print(edges)
# dist[1] = 0
# visited[1] = 0
# edge_count = 0
# mst = [1]
# curNode = 1

# while edge_count != N-1:
#     for cost, dest in edges[curNode]:
#         if visited[dest] == 0:
#             curNode = dest
#             visited[curNode] = 1
#             break
        
#     edge_count += 1

