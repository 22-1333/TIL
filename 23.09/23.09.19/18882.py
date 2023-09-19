N = int(input())
gold_list = list(map(int, input().split()))
gold_list.sort()
take_out = list()
for _ in range(2):
    take_out.append(gold_list.pop(0))
gold = 0

while type(sum(take_out)) is not float and len(gold_list) > 1:
    print(gold_list)
    print(take_out)
    gold += 2
    heavier = take_out[1]
    gold_list.append(heavier * 2 + 0.5)
    gold_list.sort()
    take_out = list()
    for _ in range(2):
        take_out.append(gold_list.pop(0))

if type(take_out[0]) is int:
    gold += 1

print(gold)
