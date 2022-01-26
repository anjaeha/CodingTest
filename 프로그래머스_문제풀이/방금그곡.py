def change(m):
    return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    answer = []
    m = change(m)
    
    for musicinfo in musicinfos:
        start, end, title, sing = musicinfo.split(',')
        sh, sm = start.split(':')
        eh, em = end.split(':')
        time = int(eh) * 60 + int(em) - (int(sh) * 60 + int(sm))
        
        sing = change(sing)
        
        sing = (sing * time)[:time]
        if m in sing:
            answer.append((time, title))
    
    answer.sort(key = lambda x : -x[0])
    if answer:
        return answer[0][1]
    else:
        return "(None)"