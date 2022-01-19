from sys import stdin

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    parent_a = find_parent(parent,a)
    parent_b = find_parent(parent,b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

n = int(stdin.readline())
m = int(stdin.readline())
answer = 0
graph = []
parent = {node:node for node in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int,stdin.readline().split())
    graph.append((a,b,c))

graph = sorted(graph,key=lambda x:x[2])
for s,e,w in graph:
    if find_parent(parent,s) == find_parent(parent,e):
        continue
    answer += w
    union_parent(parent,s,e)

print(answer)
