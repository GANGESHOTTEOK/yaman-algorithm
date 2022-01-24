from sys import stdin,setrecursionlimit
setrecursionlimit(int(1e6))

def init(start, end, node):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]

def sum(start,end,node,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start+end)//2

    return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right)

def update(start,end,node,search,value):
    if search > end or search < start:
        return
    tree[node] += value
    if start == end:
        return
    mid = (start+end)//2
    update(start,mid,node*2,search,value)
    update(mid+1,end,node*2+1,search,value)

n,m,k = map(int,stdin.readline().split())
num = [0]*n
tree = [0] * 4*n

for i in range(n):
    num[i] = int(stdin.readline())

init(0,n-1,1)

for _ in range(m+k):
    a,b,c = map(int,stdin.readline().split())
    if a==1:
        update(0,n-1,1,b-1,c-num[b-1])
        num[b-1] = c
    else:
        print(sum(0,n-1,1,b-1,c-1))
