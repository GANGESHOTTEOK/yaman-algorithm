import sys
input = sys.stdin.readline
N,d,k,c = map(int, input().split())
susi = []
for _ in range(N):
    susi.append(int(input()))
susi += susi
# print(susi)
max_kind = cur_kind = 0
start = 0
selected = [0]*(d+1)
for end in range(N*2):
    # print(susi[end], start, end, cur_kind, max_kind)
    if selected[susi[end]]==0:
        # if susi[end] != c:
        cur_kind += 1
        # print("cur increase", cur_kind)
    selected[susi[end]] += 1
    if end - start == k-1:
        # print("end - start == k-1")
        if selected[c] == 0:
            # print("include coupon kind")
            cur_kind+=1
        if max_kind < cur_kind:
            max_kind = cur_kind
            # print("max_kind update:", max_kind)
        if selected[c] == 0:
            # print("include coupon kind")
            cur_kind-=1
        selected[susi[start]] -= 1
        if selected[susi[start]] == 0:
            # print("selected[susi[start]] == 0",susi[start])
            cur_kind -= 1
        start += 1
        
print(max_kind)