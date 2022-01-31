def solution(genres, plays):
    answer = []
    genre = {}
    play = {}
    for i in range(len(genres)):
        if genres[i] in genre:
            genre[genres[i]] += plays[i]
            play[genres[i]].append([i, plays[i]])
        else:
            genre[genres[i]] = plays[i]
            play[genres[i]] = [[i, plays[i]]]

    genre = sorted(genre.items(), key=lambda x: -x[1])

    for i in range(len(genre)):
        song = genre[i][0]
        temp = play[song]
        temp.sort(key=lambda x: (-x[1], x[0]))

        if len(temp) >= 2:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])

    return answer