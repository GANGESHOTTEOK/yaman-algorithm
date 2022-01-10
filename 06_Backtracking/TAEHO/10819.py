from sys import stdin

def backtracking(cnt):
    global max_sum
    if cnt == n:
        max_sum = max(max_sum,sum([abs(back_list[i-1]-back_list[i]) for i in range(1,n)]))

    for i in range(n):
        if visit[i] == 0:
            back_list.append(array[i])
            visit[i] = 1
            backtracking(cnt+1) 
            back_list.pop()
            visit[i] = 0

n = int(stdin.readline())
visit = [0] * n
array = list(map(int,stdin.readline().split()))
back_list = []
max_sum = 0
backtracking(0)
print(max_sum)