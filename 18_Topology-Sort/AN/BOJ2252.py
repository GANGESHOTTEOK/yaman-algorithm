from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for i in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
    
topology = []
queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        
while queue:
    x = queue.popleft()
    topology.append(x)
    for student in graph[x]:
        indegree[student] -= 1
        if indegree[student] == 0:
            queue.append(student)
            
print(*topology)