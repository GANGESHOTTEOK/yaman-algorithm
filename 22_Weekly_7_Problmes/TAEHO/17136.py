from sys import stdin,maxsize

def BT(x, y, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return

    if x >= 10:
        BT(0, y+1, cnt)
        return

    if matrix[x][y] == 1:
        for k in range(5):
            if papers[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if matrix[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        matrix[i][j] = 0

                papers[k] += 1
                BT(x + k + 1, y, cnt + 1)
                papers[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        matrix[i][j] = 1
    else:
        BT(x + 1, y, cnt)


matrix = [list(map(int, stdin.readline().split())) for _ in range(10)]
papers = [0 for _ in range(5)]
ans = maxsize
BT(0, 0, 0)
print( ans if ans != maxsize else -1)