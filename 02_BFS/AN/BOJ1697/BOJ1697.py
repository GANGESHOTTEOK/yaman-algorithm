import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
queue = deque([(N,0)])
visited = set([N])
        
while queue:
    x,depth = queue.popleft()
    if x==K:
        print(depth)
        break
    for n in [x-1, x+1, 2*x]:
        if n not in visited and 0<=n<=100000:
            visited.add(n)
            queue.append((n,depth+1))