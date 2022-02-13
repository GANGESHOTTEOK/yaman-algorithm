import sys
input = sys.stdin.readline

def goSadari():
    for start in range(1,N+1):
        pole = start
        for height in range(1,H+1):
            if sadari[height][pole] == 1:
                pole += 1
            elif sadari[height][pole-1] == 1:
                pole -= 1
        if start != pole:
            return 0
    return 1

def add_line(target,current,r,c):
    global isFind,answer
    if target==current:
        isFind = goSadari()
        if isFind==1:
            answer = current
            return
    for i in range(r,H+1):
        for j in range(c,N):
            # print(i,j)
            if sadari[i][j]==0 and sadari[i][j-1]==0 and sadari[i][j+1]==0:
                sadari[i][j] = 1
                add_line(target,current+1,i,j)
                sadari[i][j] = 0
                if isFind==1:
                    return
        c=1


N,M,H = map(int,input().split())
sadari = [[0 for i in range(N+1)] for j in range(H+1)]
for _ in range(M):
    a,b = map(int,input().split())
    sadari[a][b] = 1
isFind = answer = 0
for i in range(0,4):
    if isFind==0:
        add_line(i,0,1,1)
print(answer)