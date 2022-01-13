def knapsack(N, K, cargo):
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        wi = cargo[i][0] # i번째 물건의 무게
        vi = cargo[i][1] # i번째 물건의 가치

        for w in range(K + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wi <= w:
                dp[i][w] = max(vi + dp[i - 1][w - wi], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print(dp[-1][-1])


N, K = map(int, input().split())
cargo = [(0, 0)]

for _ in range(N):
    w, v = map(int, input().split())
    cargo.append((w, v))

knapsack(N, K, cargo)