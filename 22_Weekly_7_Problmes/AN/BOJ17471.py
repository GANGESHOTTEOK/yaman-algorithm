import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# is connected zone(curZone)
def isZone(curZone):
    if len(curZone)==1:
        return True
    # bfs
    x = list(curZone)[0]
    queue = deque([x])
    curZone.remove(x)
    while queue:
        x = queue.popleft()
        for next in adj[x]:
            if next not in curZone:
                continue
            queue.append(next)
            curZone.remove(next)

    return False if curZone else True
    
# input
N = int(input())
populations = [0]+list(map(int,input().split()))
adj = [[0]]
for a in range(N):
    adj.append(list(map(int,input().split()))[1:])

min_result = sys.maxsize
cities = set(range(1,N+1))

for r in range(1,N//2+1):    # r : # of city (nCr)
    for zone in combinations(cities,r):     # get diff between zones
        temp_zone = set(zone)
        if isZone(temp_zone) and isZone(cities-set(zone)):  # if both zones are zone
            diff = 0
            for p in range(1,N+1):  
                if p in zone:                   # if p city in this zone
                    diff += populations[p]      # increase p city's population
                else:                           # if p city in that zone
                    diff -= populations[p]      # decrease p city's population
                
            min_result = min(min_result,abs(diff))
# output
print(min_result if min_result!=sys.maxsize else -1)