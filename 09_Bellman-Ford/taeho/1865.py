from sys import stdin,maxsize

def bellmanFord():
    for i in range(1,n+1):
        for j in range(1,n+1):
            for wei,vec in graph[j]:
                if dist[vec] > wei + dist[j]:
                    dist[vec] = wei + dist[j]
                    if i == n:
                        return False
    return True

tc = int(stdin.readline())

for _ in range(tc):
    n,m,w = map(int, stdin.readline().split())
    dist = [maxsize for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,t = map(int, stdin.readline().split())
        graph[s].append((t,e))
        graph[e].append((t,s))
    
    for _ in range(w):
        s,e,t = map(int,stdin.readline().split())
        graph[s].append((-t,e))
    
    result = bellmanFord()
    print("NO" if result else "YES")