import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

budgets.sort()

def getSum(limit):
    sum = 0
    for k in budgets:
        if k <= limit:
            sum += k
        else:
            sum += limit
    return sum

left, right, highest = 0, budgets[N-1], 0

while left <= right:
    mid = (left+right)//2
    total = getSum(mid)
    if total <= M:
        highest = mid
        left = mid+1
    else:
        right = mid-1

print(highest)