def solution(name):
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
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