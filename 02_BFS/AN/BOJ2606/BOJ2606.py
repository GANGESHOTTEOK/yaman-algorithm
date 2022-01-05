import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
net = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0 for i in range(N+1)]
queue = deque([1])
visited[1] = 1
count = 0

for i in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    net[X][Y] = net[Y][X] = 1
    
while queue:
    x = queue.popleft()
    for k in range(N+1):
        if visited[k]==0 and net[x][k] == 1:
            queue.append(k)
            visited[k] = 1
            count += 1
            
print(count)