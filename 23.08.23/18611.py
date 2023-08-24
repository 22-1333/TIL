N = int(input())
similar_list = [list(input().split()) for _ in range(N)]
team_list = list()

for similar in similar_list:
    for team in team_list:
        if similar[0] in team or similar[1] in team:
            if similar[0] in team and similar[1] in team:
                team.remove(similar[0])
                team.remove(similar[1])
                break
            else:
                team.add(similar[0])
                team.add(similar[1])
                break
    else:
        new_team = set()
        new_team.add(similar[0])
        new_team.add(similar[1])
        team_list.append(new_team)

musicians = 0
teams = 0
for team in team_list:
    teams += 1
    musicians += len(team)

print(teams)
print(26 - musicians)
print(team_list)
