import sys

N = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for k in target:
    if k in card:
        print('1', end=' ')
    else:
        print('0', end=' ')

# Binary Search
# import sys

# N = int(sys.stdin.readline())
# card = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# target = list(map(int, sys.stdin.readline().split()))

# card.sort()

# for k in target:
#     left = 0
#     right = len(card)-1
#     flag = 0
#     while left <= right:
#         mid = (left+right)//2
#         if card[mid] == k:
#             flag = 1
#             break
#         elif card[mid] < k:
#             left = mid+1
#         else:
#             right = mid-1
#     print(flag, end=' ')