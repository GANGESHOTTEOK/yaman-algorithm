from collections import deque
visited = [False] * 50

result = []
def back_track(data, call):
    if len(result) == 6:
        print(' '.join(map(str, result)))
        return

    for num in data:
        if not visited[num] and num > call:
            result.append(num)
            visited[num] = True
            back_track(data, num)
            visited[num] = False
            result.pop()


while True:
    input_data = deque(list(map(int, input().split())))
    if input_data[0] == 0:
        break
    input_data.popleft()
    back_track(input_data, 0)
    print()

