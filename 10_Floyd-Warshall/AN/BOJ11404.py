import sys

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[INF if i!=j else 0 for i in range(n)] for j in range(n)]


for _ in range(m):
    a,b,c = map(int, input().split())
    a -= 1; b -= 1
    graph[a][b] = min(graph[a][b],c)

for stopover in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][stopover]+graph[stopover][j])
       
print('\n'.join([' '.join([str(i) if i!=INF else '0' for i in row]) for row in graph]))