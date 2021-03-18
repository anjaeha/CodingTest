from itertools import permutations

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer :
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1

    for i in answer.values():
        cnt *= (i+1)

    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))