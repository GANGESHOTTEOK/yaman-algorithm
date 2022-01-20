import sys, heapq

class disjoint_set:
    def __init__(self, vertex_num):
        # (ID, rank, parent)
        self.forest = [[i, 0, i] for i in range(0, vertex_num+1)]

    def find(self, x) -> int:
        cur_id, cur_rank, cur_parent = self.forest[x]

        while cur_id != cur_parent:
            cur_id, cur_rank, cur_parent = self.forest[cur_parent]

        return cur_id

    def union(self, x, y) -> bool:
        root_x, root_y = self.forest[self.find(x)], self.forest[self.find(y)]

        if root_x[0] == root_y[0]:
            return True

        if root_x[1] > root_y[1]:
            root_x, root_y = root_y, root_x

        root_x[2] = root_y[0]
        root_y[1]  += 1
        return False

def kruskal(graph: dict, disjoint: disjoint_set) -> int:
    mst_weight = 0
    heap = []

    # 모든 에지를 최소힙에 넣음
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
N = int(input())
M = int(input())
graph = {i : [] for i in range(1, N+1)}
disjoint = disjoint_set(N)

for _ in range(M):
    from_, to_, weight_ = map(int, sys.stdin.readline().split())
    graph[from_].append((weight_, to_))
    graph[to_].append((weight_, from_))
#

print(kruskal(graph, disjoint))