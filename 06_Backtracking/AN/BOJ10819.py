import sys

N = int(sys.stdin.readline().rstrip())
origin = list(map(int, sys.stdin.readline().rstrip().split()))

array = []
highest = 0
visited = [0 for _ in range(N)]

def maxDiff(depth, result):
    if(depth==N):
        global highest 
        highest = max(highest, result)
        return
    for i in range(N):
        if not  visited[i]:
            visited[i] = 1
            array.append(origin[i])
            diff = 0
            if len(array)>=2:
                diff += abs(array[-1] - array[-2])
            result += diff 
            maxDiff(depth+1, result)
            result -= diff
            array.pop()
            visited[i] = 0

maxDiff(0, 0)
print(highest)