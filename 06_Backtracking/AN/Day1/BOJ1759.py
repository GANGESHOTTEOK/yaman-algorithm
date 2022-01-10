import sys

L, C = map(int, sys.stdin.readline().rstrip().split())
alphabets = list(map(str, sys.stdin.readline().rstrip().split()))

encode = []
visited = [0 for i in range(C)]
moeum = {'a', 'e', 'i', 'o', 'u'}

# cCl
def createCode(depth, moCnt):
    if depth == L:
        if 1 <= moCnt < L-1:
            for e in encode:
                print(e,end='')
            print()
        return
    k = alphabets.index(encode[-1])+1 if encode else 0
    for i in range(k,len(alphabets)):
        if not visited[i]:
            if alphabets[i] in moeum:
                moCnt += 1
                # print(moCnt)
            visited[i]=1
            encode.append(alphabets[i])
            createCode(depth+1, moCnt)
            if alphabets[i] in moeum:
                moCnt -= 1
            encode.pop()
            visited[i]=0

alphabets.sort()
createCode(0,0)