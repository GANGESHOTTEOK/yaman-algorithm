from sys import stdin

n,m = map(int,stdin.readline().split())
array = list(map(int,stdin.readline().split()))
e = 0
array_sum = 0
answer = 0
for s in range(n):
    while e < n and array_sum < m:
        array_sum += array[e]
        e += 1
    
    if array_sum == m:
        answer += 1
    array_sum -= array[s]

print(answer)