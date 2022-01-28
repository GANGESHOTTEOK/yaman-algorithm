import sys
input = sys.stdin.readline
N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int,input().split())))
array.append([0,0,0])
dp_M = [[-1]*3 for _ in range(N+1)]
dp_m = [[-1]*3 for _ in range(N+1)]
def decre(depth,i):
    if depth==0:
        return array[depth][i], array[depth][i]
    if dp_M[depth][i] != -1:
        return dp_M[depth][i], dp_m[depth][i]
    M1,m1 = decre(depth-1,1)
    if i == 0:
        M0,m0 = decre(depth-1,0)
        dp_M[depth][i] = max(M0,M1)+array[depth][i]
        dp_m[depth][i] = min(m0,m1)+array[depth][i]
        return dp_M[depth][i], dp_m[depth][i]
    M2,m2 = decre(depth-1,2)
    if i == 1:
        M0,m0 = decre(depth-1,0)
        dp_M[depth][i] = max(max(M0,M1),M2)+array[depth][i]
        dp_m[depth][i] = min(min(m0,m1),m2)+array[depth][i]
        return dp_M[depth][i], dp_m[depth][i]
    dp_M[depth][i] = max(M1,M2)+array[depth][i]
    dp_m[depth][i] = min(m1,m2)+array[depth][i]
    return dp_M[depth][i], dp_m[depth][i]

print(decre(N,1))
    
        
        
    