from sys import stdin,maxsize
import heapq as hq
#----------------Kruskal------------------#
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     parent_a = find_parent(parent,a)
#     parent_b = find_parent(parent,b)

#     if parent_a < parent_b:
#         parent[parent_b] = parent_a
#     else:
#         parent[parent_a] = parent_b

# n = int(stdin.readline())
# m = int(stdin.readline())
# answer = 0
# graph = []
# parent = {node:node for node in range(1,n+1)}
# for _ in range(m):
#     a,b,c = map(int,stdin.readline().split())
#     graph.append((a,b,c))

# graph = sorted(graph,key=lambda x:x[2])
# for s,e,w in graph:
#     if find_parent(parent,s) == find_parent(parent,e):
#         continue

#     print(s,e,w)
#     answer += w
#     union_parent(parent,s,e)

# print(answer)

#---------------- Prim ------------------#
n = int(stdin.readline())
m = int(stdin.readline())

answer = 0
q = []

visit = {node:0 for node in range(1,n+1)}
graph = {node:{} for node in range(1,n+1)}
count = 0
for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a][b] = graph[b][a] = c

hq.heappush(q,(0,1))
while count <= n-1:
    value,node = hq.heappop(q)
    if visit[node] == 1:
        continue

    count += 1
    answer += value
    visit[node] = 1
    for adj_node,adj_value in graph[node].items():
        hq.heappush(q,(adj_value,adj_node))

print(answer)