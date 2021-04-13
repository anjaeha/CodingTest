def solution(s):
    s = s.lower()
    list_s = s.split(" ")
    answer = ""

    for i in list_s:
        i = i.capitalize()
        answer += i + " "

    return answer[:-1]



print(solution("3people unFollowed me"))