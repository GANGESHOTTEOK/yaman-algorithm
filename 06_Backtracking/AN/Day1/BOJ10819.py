import sys

lotto = []
tc = []
visited = set()
def combination(depth):
    if depth == 6:
        print(*tc)
        # print()
        return
    k = lotto[-1]+1 if lotto else 0
    for x in range(k, len(tc)):
        print(x)
        if tc[x] in visited:
            continue
        visited.add(tc[x])
        lotto.append(tc[x])
        combination(depth+1)
        lotto.pop()
        visited.remove(tc[x])

while 1:
    tc = list(map(int,sys.stdin.readline().split()))
    if not tc[0]:
        break
    tc.pop(0)
    combination(0)
    
# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0

# 7 1 2 3 4 5 6 7
# 0