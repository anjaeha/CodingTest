def solution(numbers, target):
    a = [0]
    
    for i in numbers:
        b = []
        for j in a:
            b.append(j - i)
            b.append(j + i)
            
        a = b
        
    return a.count(target)