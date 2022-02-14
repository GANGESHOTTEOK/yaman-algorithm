import sys
input = sys.stdin.readline
INF = sys.maxsize

def min_init(node, start, end):
    if start == end:
        min_tree[node] = array[start]
    else:
        mid = (start + end) // 2
        min_tree[node] = min(min_init(node*2, start, mid), min_init(node*2+1, mid+1, end))
    return min_tree[node]

def max_init(node, start, end):
    if start == end:
        max_tree[node] = array[start]
    else:
        mid = (start + end) // 2
        max_tree[node] = max(max_init(node*2, start, mid), max_init(node*2+1, mid+1, end))
    return max_tree[node]

def subMin(node, start, end, left, right):
    if left > end or right < start:
        return INF
    if left <= start and right >= end:
        return min_tree[node]

    mid = (start + end) // 2
    return min(subMin(node*2, start, mid, left, right), subMin(node*2+1, mid+1, end, left, right))

def subMax(node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and right >= end:
        return max_tree[node]

    mid = (start + end) // 2
    return max(subMax(node*2, start, mid, left, right), subMax(node*2+1, mid+1, end, left, right))


min_tree = [INF for _ in range(262144)]
max_tree = [0 for _ in range(262144)]
array = []

N,M = map(int, input().split())

for _ in range(N):
    array.append(int(input()))

min_init(1,0,N-1)
max_init(1,0,N-1)

for _ in range(M):
    a,b = map(int,input().split())
    print(subMin(1,0,N-1,a-1,b-1), subMax(1,0,N-1,a-1,b-1))