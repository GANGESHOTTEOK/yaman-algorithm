import sys, heapq

# 디스조인트 셋 자료구조
class disjoint_set:
    # 그래프의 정점 개수만큼 노드 생성
    def __init__(self, vertex_num):
        # (ID, rank, parent)
        self.set = [[i, 0, i] for i in range(0, vertex_num + 1)]

    # x노드의 부모 노드 ID를 반환
    def find(self, x) -> int:
        cur = self.set[x]
        cur_id, cur_rank, cur_parent = cur[0], cur[1], cur[2]

        while cur_id != cur_parent:
            cur = self.set[cur_parent]
            cur_id, cur_rank, cur_parent = cur[0], cur[1], cur[2]

        return cur_id

    # x노드와 y노드를 union
    def union(self, x, y) -> bool:
        root_x, root_y = self.set[self.find(x)], self.set[self.find(y)]

        # x노드와 y노드의 루트가 같다면 cycle이 형성될 수 있음
        if root_x[0] == root_y[0]:
            return True

        # x노드와 y노드를 union
        if root_x[1] > root_y[1]:
            root_x, root_y = root_y, root_x

        root_x[2] = root_y[0]
        root_y[1] += 1
        return False

def kruskal(graph: dict, disjoint: disjoint_set) -> int:
    mst_weight = 0
    heap = []

    for start in range(1, len(graph) + 1):
        for weight, end in graph[start]:
            heapq.heappush(heap, (weight, start, end))

    while heap:
        edge = heapq.heappop(heap)
        weight, start, end = edge[0], edge[1], edge[2]

        if disjoint.union(start, end):
            continue

        mst_weight += weight

    return mst_weight



# 입력 부분 #
V, E = map(int, input().split())
graph = {i : [] for i in range(V+ 1)}
disjoint = disjoint_set(V)

for _ in range(E):
    from_, to_, weight_ = map(int, sys.stdin.readline().split())
    graph[from_].append((weight_, to_))
    graph[to_].append((weight_, from_))
#

print(kruskal(graph, disjoint))