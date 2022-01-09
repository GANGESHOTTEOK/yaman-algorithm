# input data
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def house_counting(graph, x, y) -> bool:
    # 범위를 벗어나면
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False
    
    # 집이 아니면
    if graph[x][y] == 0:
        return False
    
    # 집이면
    global house_cnt
    house_cnt += 1
    
    graph[x][y] = 0
    house_counting(graph, x-1, y)
    house_counting(graph, x+1, y)
    house_counting(graph, x, y-1)
    house_counting(graph, x, y+1)
    return True

# 단지의 수
complex_cnt = 0
# 단지 내 집의 수
house_cnt = 0
house = []

for i in range(N):
    for j in range(N):
        if house_counting(graph, i, j):
            house.append(house_cnt)
            house_cnt = 0
            complex_cnt += 1
            
print(complex_cnt)
house.sort()
for num in house:
    print(num)
