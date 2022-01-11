from sys import stdin

def backtracking(cnt):
    if cnt == n:
        print(" ".join(map(str,back_list)))
        return 
    
    for i in range(1,n+1):
        if visit[i] == 0:
            visit[i] = 1
            back_list[cnt] = i
            backtracking(cnt+1)
            visit[i] = 0


n = int(stdin.readline())
back_list = [0] * n
visit = [0]*(n+1)
backtracking(0)