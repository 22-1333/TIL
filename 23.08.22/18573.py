Q = int(input())
number_list = list(map(int, input().split()))
max_two = 20
max_three = 10
max_five = 10
ugly_number_set = set()

for exponent_two in range(max_two + 1):
    for exponent_three in range(max_three + 1):
        for exponent_five in range(max_five + 1):
            ugly_number_set.add((2 ** exponent_two) * (3 ** exponent_three) * (5 ** exponent_five))

ugly_number_list = sorted(ugly_number_set)
for number in number_list:
    print(ugly_number_list[number - 1], end=" ")
