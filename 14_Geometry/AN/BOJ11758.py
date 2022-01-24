import sys
input = sys.stdin.readline
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

a = (y2-y1)*(x3-x1)+y1*(x2-x1)
b = (x2-x1)*y3

if a<b:
    print(1)
elif a>b:
    print(-1)
else:
    print(0)