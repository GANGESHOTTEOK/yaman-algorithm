N = int(input())
stars = [[0 for _ in range(N)] for _ in range(N)]

def draw_stars(stars, x, y, N):
    if N == 3:
        for i in range(x, x+N):
            for j in range(y, y+N):
                if i % 3 == 1 and j % 3 == 1:
                    stars[i][j] = 0
                else:
                    stars[i][j] = 1
        return

    size = N // 3
    for i in range(3):
        for j in range(3):
            if i % 3 == 1 and j % 3 == 1:
                continue
            else:
                draw_stars(stars, x + size * i, y + size * j, size)


draw_stars(stars, 0, 0, N)
for i in range(N):
    for j in range(N):
        print(' ' if stars[i][j] == 0 else '*', end="")
    print()

