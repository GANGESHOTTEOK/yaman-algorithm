import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    info = []
    for j in range(N):
        first, second = map(int, sys.stdin.readline().split())
        info.append((first,second))
    
    info.sort()
    
    count = 0
    highest = info[0][1]
    
    for grades in info:
        if grades[1] <= highest:
            count += 1
            highest = grades[1]
    
    print(count)
    