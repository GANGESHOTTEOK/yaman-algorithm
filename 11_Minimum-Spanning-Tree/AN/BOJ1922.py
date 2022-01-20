import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())

edges = []
dist = [INF]*(N+1)
visited = [0]*(N+1)

for _ in range(M):
    edges.append(list(map(int, input().split())))
    
