def solution(clothes):
    cloth = {}
    for x, y in clothes:
        if y in cloth:
            cloth[y] += 1
        else:
            cloth[y] = 1
    
    answer = 1
    for i in cloth.values():
        answer *= (i + 1)
    return answer - 1