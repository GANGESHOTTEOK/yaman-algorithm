N = int(input())
request = list(map(int, input().split()))
M = int(input())

def max_deposit(request:list, all_deposit:int) -> int:
    if sum(request) <= all_deposit:
        return max(request)

    start = 0
    end = max(request)
    mid = (start + end) // 2
    while start < mid < end:
        total = 0
        for num in request:
            if num <= mid:
                total += num
            else:
                total += mid

        if total <= all_deposit:
            start = mid
        else:
            end = mid
        mid = (start + end) // 2

    return mid

result = max_deposit(request, M)
print(result)
