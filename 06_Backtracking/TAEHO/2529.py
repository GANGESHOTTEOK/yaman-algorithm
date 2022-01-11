from sys import stdin

def backtracking(cnt):
    global max_num,min_num
    if cnt == n+1:
        num = "".join(map(str,back_list))
        max_num = max(max_num,num)
        min_num = min(min_num,num)
        return

    for i in range(10):
        if cnt == 0:
            if visited[i] == 0:
                back_list[cnt] = i
                visited[i] = 1
                backtracking(cnt+1)
                visited[i] = 0
        elif inequals[cnt-1] == '<':
            if back_list[cnt-1] < i and visited[i] == 0:
                back_list[cnt] = i
                visited[i] = 1
                backtracking(cnt+1)
                visited[i] = 0    
        else:
            if back_list[cnt-1] > i and visited[i] == 0:
                back_list[cnt] = i
                visited[i] = 1
                backtracking(cnt+1)
                visited[i] = 0

n = int(stdin.readline())
inequals = stdin.readline().split()
max_num = "0"*(n+1)
min_num = "9"*(n+1)
back_list = [0]*(n+1)
visited = [0]*10

backtracking(0)

print(max_num,min_num,sep="\n",end="")