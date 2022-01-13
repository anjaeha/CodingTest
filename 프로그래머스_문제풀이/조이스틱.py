def solution(name):
    change = []
    for i in range(len(name)):
        change.append(min(ord(name[i]) - 65, 91 - ord(name[i])))
    
    answer = 0
    idx = 0
    
    while 1:
        answer += change[idx]
        change[idx] = 0
        
        if sum(change) == 0:
            return answer
        
        left, right = 1, 1
        
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        
        answer += min(left, right)
        
        if left < right:
            idx -= left
        else:
            idx += right