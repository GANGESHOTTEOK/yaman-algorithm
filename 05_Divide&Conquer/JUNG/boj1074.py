N, r, c = map(int, input().split())

count = 0
def get_order(x, y, size):
    global count

    if x == r and y == c:
        print(count)
        exit(0)

    if size == 1:
        count += 1
        return

    if not (x <= r < x + size and y <= c < y + size):
        count += size ** 2
        return

    N = size // 2
    get_order(x  , y  , N)
    get_order(x  , y+N, N)
    get_order(x+N, y  , N)
    get_order(x+N, y+N, N)


get_order(0, 0, 2**N)