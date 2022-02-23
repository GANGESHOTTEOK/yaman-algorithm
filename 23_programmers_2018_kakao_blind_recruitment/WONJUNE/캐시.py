def solution(cacheSize, cities):
    answer = 0
    cache = []
    for c in cities:
        c = c.upper()
        if bool(cache) and len(cache) >= cacheSize:
            if c in cache:
                cache.pop(cache.index(c))
                answer+=1
            else:
                cache.pop(0)
                answer+=5
        elif len(cache) < cacheSize:
            if c in cache:
                answer+=1
            else:
                answer+=5
        else:
            answer+=5
        if cacheSize > 0:
            cache.append(c)
    
    return answer
