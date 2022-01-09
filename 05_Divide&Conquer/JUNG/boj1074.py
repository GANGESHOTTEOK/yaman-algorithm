N, r, c = map(int, input().split())

result = 0
def func(x, y, len):
    global result

    if x == r and y == c:
        print(result)
        exit(0)

    if len == 1:
        result += 1
        return

    if not (x <= r < x + len and y <= c < y + len):
        result += (len ** 2)
        return

    size = len // 2
    func(x     , y     , size)
    func(x     , y+size, size)
    func(x+size, y     , size)
    func(x+size, y+size, size)


func(0, 0, 2**N)