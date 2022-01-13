from sys import stdin
#---------------DP--------------#
DP = [[0]*30 for _ in range(30)]

def comb(m,n):
    if DP[m][n] != 0:
        return DP[m][n]
    elif n==m or n==0:
        return 1
    else:
        DP[m][n] = comb(m-1,n-1) + comb(m-1,n)
        return DP[m][n]

T = int(stdin.readline())
for _ in range(T):
    n,m = map(int,stdin.readline().split())
    print(comb(m,n))

#---------------파이썬(>3.8)---------------#
# import sys
# import math
# answer = []
# test_case = int(input())
# for i in range(test_case):
#     west,east = map(int,sys.stdin.readline().split())
#     count = math.comb(east,west)
#     answer.append(count)

# for cnt in answer:
#     print(cnt)