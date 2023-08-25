N = int(input())
number_list = list()

for number in range(1, N + 1):
    if "3" in str(number) or "6" in str(number) or "9" in str(number):
        number_list.append("-" * (str(number).count("3") + str(number).count("6") + str(number).count("9")))
    else:
        number_list.append(str(number))

print(*number_list)
