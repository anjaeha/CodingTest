def solution(people, limit):
    people.sort()
    min_num, max_num = 0, len(people) - 1
    cnt = len(people)

    while min_num < max_num:
        if people[min_num] + people[max_num] <= limit:
            cnt -= 1
            min_num += 1
            max_num -= 1
        else:
            max_num -= 1
            
    return cnt


print(solution([70, 50, 50, 50], 100))