from sys import stdin,setrecursionlimit,maxsize
setrecursionlimit(int(1e6))

def max_init(start,end,node):
    if start == end:
        max_tree[node] = nums[start]
        return max_tree[node]
    mid = (start+end)//2
    max_tree[node] = max(max_init(start,mid,node*2), max_init(mid+1,end,node*2+1))
    return max_tree[node]

def min_init(start,end,node):
    if start == end:
        min_tree[node] = nums[start]
        return min_tree[node]

    mid = (start+end)//2
    min_tree[node] = min(min_init(start,mid,node*2), min_init(mid+1,end,node*2+1))
    return min_tree[node]

def max_search(start,end,node,left,right):
    if left > end or right < start:
        return -maxsize
    if left <= start and right >= end:
        return max_tree[node]
    
    mid = (start+end)//2
    return max(max_search(start,mid,node*2,left,right), max_search(mid+1,end,node*2+1,left,right))

def min_search(start,end,node,left,right):
    if left > end or right < start:
        return maxsize
    if left <= start and right >= end:
        return min_tree[node]
    
    mid = (start+end)//2
    return min(min_search(start,mid,node*2,left,right), min_search(mid+1,end,node*2+1,left,right))
    

n,m = map(int,stdin.readline().split())
nums = []
min_tree = [0]*n*4
max_tree = [0]*n*4
for _ in range(n):
    nums.append(int(stdin.readline()))

max_init(0,n-1,1)
min_init(0,n-1,1)

for _ in range(m):
    a,b = map(int,stdin.readline().split())
    print(min_search(0,n-1,1,a-1,b-1),max_search(0,n-1,1,a-1,b-1))
