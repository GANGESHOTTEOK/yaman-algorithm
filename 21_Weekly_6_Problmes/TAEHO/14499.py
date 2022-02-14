from sys import stdin


dict_command = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
n,m,x,y,k = map(int,stdin.readline().split())
road = []
dice = [0]*6
for _ in range(n):
    road.append(list(map(int,stdin.readline().split())))

command = list(map(int,stdin.readline().split()))

for c in command:
    
    if 0<= (x+dict_command[c][0])<n and 0<=(y+dict_command[c][1])<m:
        x, y = x + dict_command[c][0], y+dict_command[c][1]
        temp = dice[0] 
        if c == 1:
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = dice[2]
            dice[2] = temp
        elif c == 2:
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = dice[3]
            dice[3] = temp
        elif c == 3:
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = dice[1]
            dice[1] = temp
        else :
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[4]
            dice[4] = temp
        
        if road[x][y] == 0:
            road[x][y] = dice[5]
        else:
            dice[5] = road[x][y]
            road[x][y] = 0

        print(dice[0])