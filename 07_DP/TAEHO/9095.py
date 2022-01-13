from sys import stdin
from collections import deque
# -------- DP ---------#
arr = [0]*11
arr[1],arr[2],arr[3] = 1,2,4
for i in range(4,11):
    arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    print(arr[n])

# -------- BFS ------- #
able = [1,2,3]
for _ in range(T):
    n = int(stdin.readline())
    q = deque()
    q.append(0)
    count = 0
    while q:
        num = q.popleft()
        if num == n:
            count += 1
        
        for i in range(3):
            new_n = num+able[i]
            if new_n < 11:
                q.append(new_n)
    print(count)
