def solution(n, words):
    data = set([words[0]])
    now = words[0]
    
    for i in range(1, len(words)):
        if now[-1] == words[i][0] and words[i] not in data:
            data.add(words[i])
            now = words[i]
        else:
            return [i % n + 1, i // n + 1]

    return [0, 0]