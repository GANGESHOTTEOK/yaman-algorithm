from collections import deque

# 테스트 케이스의 개수 t
t = int(input())
# 가로길이 m, 세로길이 n, 배추가 심어져 있는 위치의 개수 k
m, n, k = 0, 0, 0
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y, m, n):
    if graph[x][y] == 0:
        return False

    queue = deque()

    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        front = queue.popleft()
        for i in range(4):
            nx = front[0] + dx[i]
            ny = front[1] + dy[i]
            if(nx <= -1 or ny <= -1 or nx >= m or ny >= n):
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return True


while (t > 0):
    t -= 1

    m, n, k = map(int, input().split())
    for _ in range(m):
        graph.append([0 for _ in range(n)])

    for _ in range(k):
        i, j = map(int, input().split())
        graph[i][j] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if bfs(graph, i, j, m, n) == True:
                count += 1
    print(count)
    graph = []
