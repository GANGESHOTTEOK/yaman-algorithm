import heapq

N = int(input())
weight = []
for _ in range(N):
    heapq.heappush(weight, int(input()))

result = 0
while weight:
    result = max(len(weight) * heapq.heappop(weight), result)

print(result)