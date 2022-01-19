import sys

input = sys.stdin.readline

k = int(input())
inequal = list(map(str, input().split()))

nums = []
visited = [False]*10
num = ''
max_num, min_num = "0"*(k+1), "9"*(k+1)

def createNum(depth):
    global num, max_num, min_num
    if depth == k+1:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    for i in range(10):
        if visited[i]:
            continue
        if len(num)!=0:
            if inequal[len(num)-1] == '<':
                if num[-1] > str(i):
                    continue
            else:
                if num[-1] < str(i):
                    continue
        num += str(i)
        visited[i] = True
        createNum(depth+1)
        visited[i] = False
        num = num[:-1]

createNum(0)
print(max_num)
print(min_num)