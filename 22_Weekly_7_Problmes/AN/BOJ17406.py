import sys
from itertools import permutations
input = sys.stdin.readline

# get min value per row with array
def getMinValue(array):
    min_value = 10000
    for row in array[1:]:
        min_value = min(min_value,sum(row))
    return min_value

# r,c,s
# rotate array with (r,c,s)
def rotateA(array,r,c,s):
    new = [[array[i][j] for j in range(M+1)] for i in range(N+1)] # rotated array
    
    new[r][c] = array[r][c]
    for dist in range(1,s+1):       # 거리별 가장자리
        row,col = r-dist,c-dist     # 왼쪽 상위
        for k in range(4):          # direction
            for i in range(2*dist): # 한방향 이동 횟수 == 거리*2
                next_r, next_c = row+dr[k],col+dc[k]
                new[next_r][next_c] = array[row][col]
                row,col = next_r,next_c

    return new

# input
N,M,K = map(int,input().split())
A = [[0]*(M+1)]
rotates = []
for _ in range(N):
    A.append([0]+list(map(int,input().split())))
for _ in range(K):
    rotates.append(tuple(map(int,input().split())))

dr = [0,1,0,-1]   # > < ^ <
dc = [1,0,-1,0]
min_result = 10000

# rotate 경우의 수
for rotate in permutations(rotates):
    new_array = [[A[i][j] for j in range(M+1)] for i in range(N+1)]         # rotated array
    # rotate array
    for r,c,s in rotate:
        new_array = rotateA(new_array,r,c,s)
    min_result = min(min_result,getMinValue(new_array)) # get min value
    
# output
print(min_result)