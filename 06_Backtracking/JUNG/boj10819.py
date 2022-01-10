N = int(input())
array = list(map(int, input().split()))

visited = [0] * N
result, discovered = [], []

def dfs(depth):
    if depth == N:
        result.append(sum(abs(discovered[i] - discovered[i + 1]) for i in range(N - 1)))
        return

    for i in range(N):
        if visited[i]:
            continue
        discovered.append(array[i])
        visited[i] = 1
        dfs(depth + 1)
        visited[i] = 0
        discovered.pop()

dfs(0)
print(max(result))