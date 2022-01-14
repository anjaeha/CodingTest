def solution(people, limit):
    people.sort()
    MIN, MAX = 0, len(people) - 1
    
    answer = len(people)
    
    while MIN < MAX:
        if people[MIN] + people[MAX] <= limit:
            answer -= 1
            MIN += 1
            MAX -= 1
        else:
            MIN -= 1
    return answer