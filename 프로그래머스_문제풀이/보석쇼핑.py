def solution(gems):
    start = 0
    end = 0
    setlen = len(set(gems))
    length = len(gems) + 1
    gemdict = {}

    while end < len(gems):
        if gems[end] in gemdict:
            gemdict[gems[end]] += 1
        else:
            gemdict[gems[end]] = 1

        end += 1

        if setlen == len(gemdict):
            while start < end:
                if gemdict[gems[start]] > 1:
                    gemdict[gems[start]] -= 1
                    start += 1
                elif end - start < length:
                    length = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break
    return answer