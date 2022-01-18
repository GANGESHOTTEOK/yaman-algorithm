import sys

input = sys.stdin.readline
INF = sys.maxsize
# float('inf')는 음수를 더해도 갱신되지 않음

def bellman(V, costs):
    dist = [INF] * (V+1)
    dist[1] = 0
    for i in range(V):
        for cur, dest, cost in costs:
            if dist[dest] > dist[cur] + cost:
                dist[dest] = dist[cur] + cost
                if i == V-1:
                    return True
    return False

TC = int(input())

for _ in range(TC):
    N,M,W = map(int, input().split())
    times = []
    for i in range(M):
        S,E,T = map(int, input().split())
        times.append((S,E,T))
        times.append((E,S,T))
    for j in range(W):
        S,E,T = map(int, input().split())
        times.append((S,E,T*(-1)))
        
    print("YES" if bellman(N,W+2*M,times) else "NO")
    
