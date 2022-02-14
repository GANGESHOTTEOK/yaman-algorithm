def solution(stones, k):
    start = 0
    end = max(stones)
    
    while start <= end:
        mid = (start + end)//2
        arr = list(map(lambda x: x-mid, stones))
        cnt = 0
        for a in arr:
            if cnt < k:
                if a <= 0:
                    cnt += 1
                else:
                    cnt = 0
            else:
                break
        if cnt < k:
            start = mid+1
        else:
            end = mid-1
            answer = mid
    return answer
