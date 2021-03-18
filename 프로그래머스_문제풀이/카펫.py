def solution(brown, yellow):
    answer = []
    
    for yellow_height in range(1, int(yellow ** 0.5) + 1):
        if yellow % yellow_height == 0:
            yellow_width = yellow // yellow_height

            if (2 * yellow_width) + (2 * yellow_height) + 4 == brown:
                answer = [yellow_width + 2, yellow_height + 2]
                break

    return answer

print(solution(5000, 2497))
