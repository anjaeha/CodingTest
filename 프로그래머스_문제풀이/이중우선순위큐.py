def solution(ops):
    answer = []

    for op in ops:
        command, number = op.split()
        if command == 'I':
            answer.append(int(number))
        else:
            if answer:
                if number == "-1":
                    answer.remove(min(answer))
                else:
                    answer.remove(max(answer))

    if answer:
        MAX = max(answer)
        MIN = min(answer)
    else:
        MAX, MIN = 0, 0

    return [MAX, MIN]