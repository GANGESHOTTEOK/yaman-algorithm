from sys import stdin,setrecursionlimit,maxsize
setrecursionlimit(int(1e6))

def init(start,end,node):
    if start == end:
        max_tree[node] = min_tree[node] = nums[start]
        return

    mid = (start+end)//2
    init(start,mid,node*2)
    init(mid+1,end,node*2+1)
    max_tree[node] = max(max_tree[node*2], max_tree[node*2+1])
    min_tree[node] = min(min_tree[node*2], min_tree[node*2+1])

def search(start,end,node,left,right):
    if left > end or right < start:
        return (maxsize,-maxsize)
    if left <= start and right >= end:
        return (min_tree[node],max_tree[node])
    
    mid = (start+end)//2
    l = search(start,mid,node*2,left,right)
    r = search(mid+1,end,node*2+1,left,right)
    return min(l[0],r[0]), max(l[1],r[1])
    
n,m = map(int,stdin.readline().split())
nums = []
min_tree = [0]*n*4
max_tree = [0]*n*4
for _ in range(n):
    nums.append(int(stdin.readline()))

init(0,n-1,1)

for _ in range(m):
    a,b = map(int,stdin.readline().split())
    print(" ".join(map(str,search(0,n-1,1,a-1,b-1))))
