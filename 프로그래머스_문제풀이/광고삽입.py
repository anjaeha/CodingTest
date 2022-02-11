def solution(play_time, adv_time, logs):
    playSec = str2int(play_time)
    advSec = str2int(adv_time)
    clock = [0] * (playSec + 1)

    for log in logs:
        temp = log.split('-')
        start = str2int(temp[0])
        end = str2int(temp[1])
        clock[start] += 1
        clock[end] -= 1

    for i in range(1, len(clock)):
        clock[i] += clock[i - 1]

    currSum = sum(clock[:advSec])
    maxSum = currSum
    maxIdx = 0

    for i in range(advSec, playSec):
        currSum = currSum + clock[i] - clock[i - advSec]
        if currSum > maxSum:
            maxSum = currSum
            maxIdx = i - advSec + 1

    return int2str(maxIdx)


def int2str(time):
    hours = time // 3600
    minutes = time % 3600 // 60
    seconds = time % 3600 % 60
    return str(hours).zfill(2) + str(':') + str(minutes).zfill(2) + str(':') + str(seconds).zfill(2)


def str2int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)