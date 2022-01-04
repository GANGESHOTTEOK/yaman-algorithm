# Depth-First Search (DFS, 깊이 우선 탐색)

## DFS의 개념
- 어떤 정점을 방문하여 확인한 후 그 정점과 연결된 정점들 중에서 우선 순위가 가장 빠른 하나를 선택해 방문해 나가는데, 더 이상 방문할 곳이 없으면 이전 상태로 되돌아가는 탐색 방법
- 이름 그대로 특정 분기의 가장 깊숙한 곳까지 탐색한 후 다음 분기로 넘어간다.
- 그래프 탐색 기법 중 하나이다.  
![image](https://mblogthumb-phinf.pstatic.net/20160203_126/lhm0812_1454503544423VyFH7_PNG/1111.png?type=w2)


## DFS의 특징
- BFS(너비 우선 탐색)에 비하여 좀 더 간단하고, 단순 검색속도는 더 느리다.
- 특정 노드에 대한 방문 여부를 저장해야한다.
### 장점
- 현재 탐색 중인 노드들의 정보만 기억하면 되기 때문에 비교적 저장 공간의 수요가 적다.
- 찾고자 하는 노드가 깊은 단계에 있을 경우 해를 빨리 구할 수 있다. ~~마지막즈음에 찾아질 경우는 소용없다.~~
### 단점
- 깊이가 무한할 경우 해를 찾을 수 없을 수도 있다. 따라서 실제로는 미리 지정한 임의 깊이까지만 탐색하고 목표 노드를 발견하지 못하면 다음 경로를 따라 탐색하는 방법이 유용할 수 있다.
- 해가 여러 개일 경우, 얻어진 해가 최단 경로가 아닐 수도 있다. 이는 목표에 이르는 경로가 다수인 문제에 대해 깊이우선탐색은 해에 다다르면 탐색을 끝내버리기 때문이다. 최단 경로를 구하기 위해서는 구한 해의 경로를 저장한 다음 최적해를 구해야한다.
### 시간 복잡도
- 노드의 수: N, 간선의 수: E
    - 인접 리스트 : O(N+E)
    - 인접 행렬 : O(N^2)
### 사용 예시
- 미로 탐색
- 괄호 검사
- 순환 그래프(circular graph) 검사
- 자동 미로 생성
- 트리의 순회(traversal)
- 조합(combination)

## DFS의 구현
- `recursive call`나 `stack`을 통해 구현할 수 있다.
- `recursive call`을 이용한 DFS 구현
``` Python
def dfs(graph, start, visited=set()):
    if start not in visited:            // 이전에 방문한 노드가 아닐 경우
        visited.add(start)              // 방문한 노드에 현재 노드 추가
        print(start, end='')
        nbr = graph[start] - visited    // 이미 방문한 노드를 제외한 인접 노드
        for v in nbr:                   // nbr 탐색
            dfs(graph, v, visited)
```
- `stack`을 이용한 DFS 구현
``` Python
def dfs(graph, start, visited=set()):
    stack = Stack()
    stack.push(start)
    while not stack.isEmpty():
        current = stack.pop()
        visited.push(current)
        nbr = graph[current] - visited
        for v in nbr:
            stack.push(v)
            visited.push(v)
```