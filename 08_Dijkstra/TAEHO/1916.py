from sys import stdin,maxsize
import heapq as hq

def dijacstra(start):
    distances = {node:maxsize for node in range(1,n+1)}
    distances[start] = 0
    q= []
    hq.heappush(q,(distances[start],start))
    while q:
        current_distance,node = hq.heappop(q)
        if current_distance > distances[node]:
            continue

        for adjancancy_node, distance in city[node].items():
            weighted_distance = current_distance + distance
            if weighted_distance < distances[adjancancy_node]:
                distances[adjancancy_node] = weighted_distance
                hq.heappush(q,(weighted_distance,adjancancy_node))

    return distances

n = int(stdin.readline())
m = int(stdin.readline())

city = {node:{} for node in range(1,n+1)}
for _ in range(m):
    s,e,v = map(int,stdin.readline().split())
    if e in city[s]:
        city[s][e] = min(city[s][e],v)
    else:
        city[s][e] = v

start,end = map(int,stdin.readline().split())
result = dijacstra(start)
print(result[end])