N = int(input())
M = int(input())
relationship = [list(map(int, input().split())) for _ in range(M)]
coco = int(input())

adj_dict = dict()
for num in range(1, N + 1):
    adj_list = list()
    for members in relationship:
        if num in members:
            adj_list.append(members[int(not(members.index(num)))])
    adj_list.sort()
    adj_dict[num] = adj_list

visited = [0] * (N + 1)
visited[coco] = 1
queue = [coco]
member = 0

while queue:
    connection_1 = queue.pop(0)

    for connection_2 in adj_dict[connection_1]:
        if not visited[connection_2]:
            member += 1
            visited[connection_2] = 1
            queue.append(connection_2)

print(member)
