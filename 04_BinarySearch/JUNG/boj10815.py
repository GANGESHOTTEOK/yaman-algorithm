import heapq
import sys

N = int(input())
heap = list(map(int, sys.stdin.readline().split()))
M = int(input())
data = list(map(int, sys.stdin.readline().split()))

arr = []

heapq.heapify(heap)
while heap:
    arr.append(heapq.heappop(heap))

def binary_serch(arr:list, target:int) -> bool:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            start = mid + 1
        if arr[mid] > target:
            end = mid - 1
    return False

for num in data:
    print(1 if binary_serch(arr, num) else 0, end=" ")