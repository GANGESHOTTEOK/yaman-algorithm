# dfs 기반 그래프 탐색
# 각 단지내 집의 수를 반환
def dfs(graph: list, bound: int, x: int, y: int) -> int:
    # 만약 해당 노드가 0이 아니면 탐색 진행
    if graph[x][y] == 0:
        return 0
    else:
        # 탐색 진행
        cnt = 0
        stack = []
        # 시작 노드를 스택에 넣고 방문처리
        stack.append((x, y))
        graph[x][y] = 0
        cnt += 1
        # 상, 하, 좌, 우 좌표를 구하기 위한 리스트
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 스택이 빌 때까지 반복
        while stack:
            # 스택의 최상단 노드를 주목
            x, y = stack[-1]
            visitFlag = False
            # 해당 노드의 상, 하, 좌, 우를 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위를 벗어나면 무시
                if nx <= -1 or nx >= bound or ny <= -1 or ny >= bound:
                    continue

                # 인접 노드(상, 하, 좌, 우)노드들 중 방문하지 않은 노드 (값이 1인 노드)가 있으면
                # 스택에 넣고 방문처리
                if graph[nx][ny] == 1:
                    stack.append((nx, ny))
                    graph[nx][ny] = 0
                    visitFlag = True
                    cnt += 1

            # 만약 방문한 노드가 없으면 최상단 노드를 pop
            if visitFlag == False:
                stack.pop()
        return cnt


if __name__ == '__main__':
    # 데이터 입력
    n = int(input())
    # 지도를 그래프로 표현
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    result = 0      # 총 단지 수
    cnt = []        # 각 단지내 집의 수

    # 노드를 하나씩 주목
    for i in range(n):
        for j in range(n):
            num = dfs(graph, n, i, j)
            # 주목 노드에서 탐색이 시작되면 0이 아닌 값, 즉 단지내 집의 수를 반환함
            if num != 0:
                result += 1
                cnt.append(num)

    cnt.sort()
    print(result)
    for num in cnt:
        print(num)
