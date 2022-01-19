from sys import stdin

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
v,e = map(int,stdin.readline().split())
graph = []
parent = {node:node for node in range(1,v+1)}
for _ in range(e):
    a,b,c = map(int,stdin.readline().split())
    graph.append((a,b,c))

graph = sorted(graph,key=lambda x:x[2])

for s,e,w in graph:
    if find_parent(parent,s) == find_parent(parent,e):
        continue
    union_parent(parent,s,e)
    answer += w

print(answer)