import sys

input = sys.stdin.readline

N = int(input())
G = []

for _ in range(N):
    G.append(list(map(int, input().split())))

for stopover in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                continue
            if G[i][stopover]*G[stopover][j] == 1:
                G[i][j] = 1

print('\n'.join([' '.join([str(i) for i in row]) for row in G]))