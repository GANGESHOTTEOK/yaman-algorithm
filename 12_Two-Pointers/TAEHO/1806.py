from sys import stdin,maxsize

min_length = maxsize

n,s = map(int,stdin.readline().split())
array = list(map(int,stdin.readline().split()))

end = 0
array_sum = array[0]

for start in range(n):
    while end<n-1 and array_sum < s:
        end += 1
        array_sum += array[end]
    
    if array_sum >= s:
        min_length = min(min_length,end-start+1)
    
    array_sum -= array[start]

print(0 if min_length == maxsize else min_length)
