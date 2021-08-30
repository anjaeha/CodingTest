from itertools import combinations
from bisect import bisect_left

def solution(infos, queries):
    answer = []
    info_dict = {}
    for info in infos:
        temp = info.split()
        info_key = temp[:-1]
        info_val = temp[-1]
        
        for i in range(5):
            for c in combinations(info_key, i):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(info_val))
                else:
                    info_dict[tmp] = [int(info_val)]
                    
    for k in info_dict:
        info_dict[k].sort()

        
    for query in queries:
        temp = query.split()
        query_key = temp[:-1]
        query_val = temp[-1]
        
        while 'and' in query_key:
            query_key.remove('and')
        while '-' in query_key:
            query_key.remove('-')
            
        query_key = ''.join(query_key)
        
        if query_key in info_dict:
            scores = info_dict[query_key]
            
            if scores:
                enter = bisect_left(scores, int(query_val))
                
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
            
    return answer