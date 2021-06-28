def control(m):
    return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    answer = []
    m = control(m)
    for i in musicinfos:
        start, end, name, s = i.split(",")
        n = abs((int(start[:2]) * 60 + int(start[3:])) - (int(end[:2]) * 60 + int(end[3:])))
        s = control(s)
        
        music = ''
        for j in range(n):
            music += s[j%len(s)]
        if music.find(m) != -1:
            answer.append((name, n))
    
    if not answer:
        return "(None)"
    
    answer.sort(reverse = True, key = lambda x : x[1])
    return answer[0][0]

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))