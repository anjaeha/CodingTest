def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    cache = []
    city = []
    for i in cities:
        city.append(i.lower())
    
    for i in city:
        if i in cache:
            answer += 1
            temp = cache.index(i)
            cache.append(cache.pop(temp))
        else:
            answer += 5
            if len(cache) == cacheSize and cache != []:
                cache.pop(0)
            cache.append(i)
    return answer