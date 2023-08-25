import copy


def less_than_three(testing):
    testing_number = 0

    for digit in range(len(testing)):
        testing_number += testing[digit] * (10 ** digit)

    if testing_number // 10 < 1:
        return True
    else:
        if abs((testing_number // 10) % 10 - (testing_number % 10)) <= 3:
            return less_than_three(list(map(int, str(testing_number // 10))))
        else:
            return False


def make_list(former_list, numbers):
    new_list = []
    if len(former_list[0]) == 4:
        return former_list
    else:
        for each_list in former_list:
            for each_number in numbers:
                temp = copy.deepcopy(each_list)
                temp.append(each_number)
                new_list.append(temp)
        return make_list(new_list, numbers)


number_list = list(map(int, str(input())))
first_list = list()
for number in number_list:
    first_list.append([number])

every_list = make_list(first_list, number_list)
counting = len(every_list)

for test in every_list:
    is_false = less_than_three(test)
    if is_false is False:
        counting -= 1

print(counting)
