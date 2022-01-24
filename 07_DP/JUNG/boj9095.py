def one_two_three(n):
    dp = [0] * 12
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

tc = int(input())
while tc:
    tc -= 1

    n = int(input())
    print(one_two_three(n))