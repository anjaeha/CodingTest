from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(users[i]):
            return False

        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for users in permutations(user_id, len(banned_id)):
        if not check(users, banned_id):
            continue

        users = set(users)
        if users not in answer:
            answer.append(users)

    return len(answer)