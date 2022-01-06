def solution(nums):
    take = len(nums) // 2 # 가지고 갈 수 있는 포켓몬의 개수
    num = set(nums) # 포켓몬의 종류
    
    return min(take, len(num))