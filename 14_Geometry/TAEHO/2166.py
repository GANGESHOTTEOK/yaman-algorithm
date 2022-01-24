from sys import stdin

n = int(stdin.readline())
x_coor,y_coor = [],[]
answer = 0
for _ in range(n):
    x,y = map(int,stdin.readline().split())
    x_coor.append(x)
    y_coor.append(y)

x_coor.append(x_coor[0])
y_coor.append(y_coor[0])

for i in range(n):
    answer += (x_coor[i]*y_coor[i+1]) - (x_coor[i+1] * y_coor[i])
print(abs(round(answer/2,1)))
