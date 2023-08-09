sentence = input()
name = str()
number = 0
name_counting = 0
number_counting = 0
prisoner_list = list()

for idx in range(len(sentence) - 1, -1, -1):
    try:
        number += int(sentence[idx]) * (10 ** number_counting)
        if name != "":
            prisoner_list.append(name[::-1])
        name_counting = 0
        name = str()
        number_counting += 1
    except ValueError:
        if number != 0:
            prisoner_list.append(number + 17)
        number_counting = 0
        number = 0
        name += sentence[idx]
prisoner_list.append(name[::-1])

for printing in range(len(prisoner_list) // 2):
    print(f"{prisoner_list[-(printing * 2 + 1)]}#{str(prisoner_list[-(printing * 2 + 2)])}")
