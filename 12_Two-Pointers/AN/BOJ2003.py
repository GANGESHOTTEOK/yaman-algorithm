import sys

input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
start = end = partial = count = 0

while end <= N:
    print(start, end, partial)
    if partial >= M:
        print("increase start")
        partial -= A[start]
        start += 1
    else:
        print("increase end")
        partial += A[end]
        end += 1
    if partial == M:
        print("increase count")
        count += 1
    
print(count)