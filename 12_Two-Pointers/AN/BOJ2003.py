import sys

input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))

start = end = part_sum = count = 0

while True:
    if part_sum >= M:
        part_sum -= A[start]
        start += 1
    elif end==N:
        break
    else:
        part_sum += A[end]
        end += 1
    if part_sum == M:
        count += 1
    
print(count)