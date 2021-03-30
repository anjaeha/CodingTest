from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

s = []
for i in range(n):
    s.append(list(map(int, input().split())))

members = [i for i in range(n)]
p_team = []

for team in list(combinations(members, n // 2)):
    p_team.append(team)

min_stat = 101
for i in range(len(p_team) // 2):
    team = p_team[i]
    stat_A = 0
    for j in range(n // 2):
        member = team[j]
        for k in team:
            stat_A += s[member][k]

    team = p_team[-i-1]
    stat_B = 0
    for j in range(n // 2):
        member = team[j]
        for k in team:
            stat_B += s[member][k]

    min_stat = min(min_stat, abs(stat_A - stat_B))

print(min_stat)