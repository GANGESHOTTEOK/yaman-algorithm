from sys import stdin

p = []

for _ in range(3):
    x,y = map(int,stdin.readline().split())
    p.append((x,y))

AB = (p[1][0]-p[0][0],p[1][1]-p[0][1])
BC = (p[2][0]-p[1][0],p[2][1]-p[1][1])

ABXBC = AB[0] * BC[1] - AB[1] * BC[0]

if ABXBC > 0:
    print(1)
elif ABXBC == 0:
    print(0)
else:
    print(-1)