import sys
input = sys.stdin.readline

def treeInit(node, start, end): 
    if start == end:
        tree[node] = array[start]
        return tree[node]
    else:
        tree[node] = treeInit(node*2, start, (start+end)//2) + treeInit(node*2+1, (start+end)//2+1, end)
        return tree[node]

def treeSubSum(node, start, end, left, right):
    # print(node, start, end, left, right)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return treeSubSum(node*2, start, (start+end)//2, left, right) + treeSubSum(node*2+1, (start+end)//2+1, end, left, right)

def treeUpdate(node, start, end, index, diff):
    if index < start or index>end:
        return
    tree[node] += diff
    if start != end :
        treeUpdate(node*2, start, (start+end)//2, index, diff)
        treeUpdate(node*2+1, (start+end)//2+1, end, index, diff)
        
N,M,K = map(int, input().split())
tree = [0]*3000000
array = []
for _ in range(N):
    array.append(int(input()))
treeInit(1,0,N-1)
# print('\n'.join(str(node)+": "+str(tree[node]) for node in range(2*(N)+1)))
for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        diff = c - array[b-1]
        array[b-1] = c
        treeUpdate(1,0,N-1,b-1,diff)
        # print(array)
        # print('\n'.join(str(node)+": "+str(tree[node]) for node in range(2*(N))))
    else:
        print(treeSubSum(1,0,N-1,b-1,c-1))