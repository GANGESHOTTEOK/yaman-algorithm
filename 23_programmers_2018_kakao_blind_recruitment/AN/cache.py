from collections import defaultdict

def solution(cacheSize, cities):
    answer = count = 0
    cache = defaultdict(int)
    
    if not cacheSize:
        return len(cities)*5
    
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
        else:
            answer += 5
            if len(cache) == cacheSize:
                discarded = [k for k,v in cache.items() if min(cache.values()) == v]
                cache.pop(discarded[0])
        cache[city] = count
        count += 1
        
    return answer