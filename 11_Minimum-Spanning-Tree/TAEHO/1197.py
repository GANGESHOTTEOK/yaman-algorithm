from sys import stdin
import heapq as hq
#-----------------kruskal MST-----------------#
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# answer = 0
# v,e = map(int,stdin.readline().split())
# graph = []
# parent = {node:node for node in range(1,v+1)}
# for _ in range(e):
#     a,b,c = map(int,stdin.readline().split())
#     graph.append((a,b,c))

# graph = sorted(graph,key=lambda x:x[2])

# for s,e,w in graph:
#     if find_parent(parent,s) == find_parent(parent,e):
#         continue
#     union_parent(parent,s,e)
#     answer += w

# print(answer)

#-----------------Prim MST------------------#

v,e = map(int,stdin.readline().split())
graph = {node:{} for node in range(1,v+1)}
visit = {node:0 for node in range(1,v+1)}
q = []
count = 0
answer = 0
for _ in range(e):
    a,b,c = map(int,stdin.readline().split())
    if b in graph[a]:
        graph[a][b] = graph[b][a] = min(graph[a][b],c)
    else:
        graph[a][b] = graph[b][a] = c

hq.heappush(q,(0,1))
while q and count <= v-1:
    cost, node = hq.heappop(q)
    if visit[node] == 1:
        continue

    visit[node] = 1
    count += 1
    answer += cost
    for adj_node, adj_cost in graph[node].items():
        hq.heappush(q,(adj_cost,adj_node))

print(answer)