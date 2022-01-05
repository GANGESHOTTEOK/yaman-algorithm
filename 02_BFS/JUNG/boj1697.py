from collections import deque
n, k = map(int, input().split())

def hide_and_seek(n, k, visited = [False] * 100001):
    queue = deque()
    queue.append(n)
    visited[n] = True

    sec = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            front = queue.popleft()
            d1, d2, d3 = front-1, front+1, front*2

            if  0 <= d1 <= 100000 and not visited[d1]:
                if d1 == k:
                    return sec
                queue.append(d1)
                visited[d1] = True

            if 0 <= d2 <= 100000 and not visited[d2]:
                if d2 == k:
                    return sec
                queue.append(d2)
                visited[d2] = True

            if 0 <= d3 <= 100000 and not visited[d3]:
                if d3 == k:
                    return sec
                queue.append(d3)
                visited[d3] = True
        sec += 1
    return 0

print(hide_and_seek(n,k))
