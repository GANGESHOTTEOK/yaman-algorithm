import sys
input = sys.stdin.readline
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

CCW = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

if CCW>0:
    print(1)
elif CCW<0:
    print(-1)
else:
    print(0)