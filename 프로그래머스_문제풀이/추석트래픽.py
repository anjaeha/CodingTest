def solution(lines):
    answer = -1
    start_time = []
    end_time = []
    for line in lines:
        line = line.split()
        h, m, s = int(line[1][:2]), int(line[1][3:5]), float(line[1][6:12])
        t = int(float(line[2][:-1]) * 1000)

        end = int((h * 3600 + m * 60 + s) * 1000)
        start = end - t + 1

        start_time.append(start)
        end_time.append(end)

    for i in range(len(lines)):
        count = 0
        for j in range(i, len(lines)):
            if end_time[i] > start_time[j] - 1000:
                count += 1
        answer = max(answer, count)

    return answer