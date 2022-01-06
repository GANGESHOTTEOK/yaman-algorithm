import heapq
import sys

TC = int(input())
while TC > 0:
    TC -= 1

    grade = []
    N = int(input())
    for _ in range(N):
        doc_grade, meet_grade = map(int, sys.stdin.readline().split())
        heapq.heappush(grade, (doc_grade, meet_grade))

    doc_grade, meet_grade = heapq.heappop(grade)
    max_meet_grade = meet_grade
    count = 1

    while grade:
        doc_grade, meet_grade = heapq.heappop(grade)
        if meet_grade < max_meet_grade:
            max_meet_grade = meet_grade
            count += 1

    print(count)