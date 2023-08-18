N = int(input())
T = int(input())
relationship_list = [list(map(int, input().split())) for _ in range(T)]
coco = int(input())
partner = int(input())
queue = [coco]
is_familiar = False

while queue:
    start = queue.pop(0)
    for relationship in relationship_list:
        if start in relationship:
            relationship.remove(start)
            end = relationship.pop()
            if end not in queue:
                queue.append(end)
                if end == partner:
                    is_familiar = True

if is_familiar:
    print("YES")
else:
    print("NO")
