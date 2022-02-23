from collections import deque
def solution(cacheSize, cities):
    q = deque()
    city_set = set()
    time = 0
    cities = map(lambda x: x.lower(),cities)
    for city in cities:
        if city in city_set:
            time += 1
            q.remove(city)
            q.appendleft(city)
        else:
            city_set.add(city)
            if len(q) < cacheSize:
                q.appendleft(city)
            else:
                q.appendleft(city)
                city_set.remove(q.pop())
            time += 5
            
    return time