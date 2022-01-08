N = int(input())
array = [["*" for _ in range(N)] for _ in range(N)]

def print_star(array, x, y, n):
    if n == 3:
        array[x + 1][y + 1] = " "
    else:
        temp = n // 3
        for i in range(x + temp, x + 2 * temp):
            for j in range(y + temp, y + 2 * temp):
                array[i][j] = " "
        for i in range(0, n, temp):
            for j in range(0, n, temp):
                print_star(array, x + i, y + j, temp)



print_star(array, 0, 0, N)
for i in range(0, N):
    for j in range(0, N):
        print(array[i][j], end="")
    print()