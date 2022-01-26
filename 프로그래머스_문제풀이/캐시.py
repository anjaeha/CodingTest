from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0
    q = deque()
    
    for city in cities:
        city = city.lower()
        if len(q) != cacheSize:
            if city in q:
                answer += 1
                q.remove(city)
                q.append(city)
            else:
                q.append(city)
                answer += 5
        else:
            if city in q:
                q.remove(city)
                q.append(city)
                answer += 1
            else:
                q.popleft()
                q.append(city)
                answer += 5

    return answer