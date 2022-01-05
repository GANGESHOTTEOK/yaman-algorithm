import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
net = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    net[X][Y] = net[Y][X] = 1
    
count = 1
queue = deque([K])
visited = set([K])

while queue:
    x = queue.popleft()
    visited.add(x)
    print("x "+str(x))
    for e in net[x]:
        print(e)
        if e not in visited and e == 1:
            queue.append(e)
            visited.add(e)
            count += 1
            
print(count)