import sys

input = sys.stdin.readline

V,E = map(int, input().split())
edges = [] # (cost, start, end)
ex = [i for i in range(0,V+1)]
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

for _ in range(E):
    A,B,C = map(int, input().split())
    edges.append((C,A,B))

edges.sort()

for cost,start,end in edges:
    if find(start) != find(end):
        union(start, end)
        min_val += cost
    
print(min_val)