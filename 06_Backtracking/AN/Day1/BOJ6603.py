import sys

lotto = []
tc = []
visited = set()
def combination(depth):
    if depth == 6:
        print(*lotto)
        return
    k = tc.index(lotto[-1])+1 if lotto else 0
    for x in range(k, len(tc)):
        if tc[x] not in visited:
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
    print()