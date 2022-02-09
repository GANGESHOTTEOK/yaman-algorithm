from sys import stdin

def row(i):
    slope = [0] * n
    for j in range(n-1):
        if abs(road[i][j] - road[i][j+1]) > 1:
            return 0

        if road[i][j] < road[i][j+1]:
            for k in range(l):
                if j-k <0 or slope[j-k]!=0:
                    return 0
                elif road[i][j-k] != road[i][j]:
                    return 0
            
            for k in range(l):
                slope[j-k] = 1
            
        elif road[i][j] > road[i][j+1]:
            for k in range(l):
                if j+k+1 >= n or slope[j+k+1]!=0:
                    return 0
                elif road[i][j+k+1] != road[i][j+1]:
                    return 0

            for k in range(l):
                slope[j+k+1] = 1
            
    return 1

def col(i):
    slope = [0] * n
    for j in range(n-1):
        if abs(road[j][i] - road[j+1][i]) > 1:
            return 0

        if road[j][i] < road[j+1][i]:
            for k in range(l):
                if j-k <0 or slope[j-k]!=0:
                    return 0
                elif road[j-k][i] != road[j][i]:
                    return 0
            
            for k in range(l):
                slope[j-k] = 1
        
        elif road[j][i] > road[j+1][i]:
            for k in range(l):
                if j+k+1 >= n or slope[j+k+1]!=0:
                    return 0
                elif road[j+k+1][i] != road[j+1][i]:
                    return 0

            for k in range(l):
                slope[j+k+1] = 1

    return 1

n, l = map(int,stdin.readline().split())

road = []
answer = 0
for _ in range(n):
    road.append(list(map(int,stdin.readline().split())))

for i in range(n):
    answer += row(i)
    answer += col(i)
print(answer)

