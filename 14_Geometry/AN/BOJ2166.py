import sys
input = sys.stdin.readline
def getCCW(x1,y1,x2,y2,x3,y3):
    return x1*y2+x2*y3+x3*y1-(x2*y1+x3*y2+x1*y3)
N = int(input())
X = [0]*(N+1)
Y = [0]*(N+1)
for i in range(N):
    X[i], Y[i] = map(int, input().split())
area = 0
X[N],Y[N] = X[0],Y[0]
for i in range(N):
    area += getCCW(0,0,X[i],Y[i],X[i+1],Y[i+1])
print(round(abs(area/2),1))