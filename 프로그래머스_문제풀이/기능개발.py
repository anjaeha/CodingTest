import math
def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    front = 0
    for idx in range(len(days)):
        if days[front] < days[idx]:
            answer.append(idx - front)
            front = idx
            
    answer.append(len(days) - front)
   
        
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))