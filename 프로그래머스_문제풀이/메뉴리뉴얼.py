from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        
        if counter:
            max_ = max(list(counter.values()))
            if max_ >= 2:
                for key, value in counter.items():
                    if counter[key] == max_:
                        answer.append(''.join(key))
        
    return sorted(answer)