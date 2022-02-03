def solution(stones, k):
    left = 0
    right = 200000000
    mid = (left+right)//2
    while left < right:
        cnt = 0
        for stone in stones:
            if stone-mid <= 0:
                cnt += 1
            else:
                cnt = 0
                
            if cnt == k:
                right = mid
                break
        else:
            left = mid+1
        
        mid = (left+right)//2
    return mid