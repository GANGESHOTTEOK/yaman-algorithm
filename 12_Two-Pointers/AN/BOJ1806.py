import sys

input = sys.stdin.readline

N,S = map(int, input().split())
seq = list(map(int,input().split()))

start=end=part_sum=0
min_len = sys.maxsize

while True:
    if part_sum >=S:
        part_sum -= seq[start]
        start += 1
    elif end == N:
        break
    else:
        part_sum += seq[end]
        end += 1
    if part_sum >= S:
        min_len = min(min_len, end-start)
        
print(min_len if min_len != sys.maxsize else 0)