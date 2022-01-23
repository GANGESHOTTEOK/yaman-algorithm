from sys import stdin

input = stdin.readline().rstrip

N = int(input())

nums = []
visited = [False]*(N+1)

def permutation(depth):
    if depth==N:
        print(*nums)
        return
    for i in range(1,N+1):
        if visited[i]:
            continue
        nums.append(i)
        visited[i] = True
        permutation(depth+1)
        visited[i] = False
        nums.pop()

permutation(0)