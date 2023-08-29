N = int(input())
sample_list = list(map(int, input().split()))
contaminated_list = list()
solution_list = list()

for sample in sample_list:
    if sample >= 0:
        solution_list.append(sample)
    else:
        contaminated_list.append(sample)

if not solution_list:
    best_pair = (contaminated_list[0], contaminated_list[1])
    for contaminated in contaminated_list:
        for other_contaminated in contaminated_list:
            if contaminated != other_contaminated:
                if sum(best_pair) < contaminated + other_contaminated:
                    if contaminated > other_contaminated:
                        best_pair = other_contaminated, contaminated
                    else:
                        best_pair = contaminated, other_contaminated
elif not contaminated_list:
    best_pair = (solution_list[0], solution_list[1])
    for solution in solution_list:
        for other_solution in solution_list:
            if solution != other_solution:
                if sum(best_pair) > solution + other_solution:
                    if solution > other_solution:
                        best_pair = other_solution, solution
                    else:
                        best_pair = solution, other_solution
else:
    best_pair = (contaminated_list[0], solution_list[0])
    for contaminated in contaminated_list:
        for solution in solution_list:
            if abs(0 - sum(best_pair)) > abs(0 - (contaminated + solution)):
                best_pair = contaminated, solution
            elif abs(0 - sum(best_pair)) == abs(0 - (contaminated + solution)):
                if abs(best_pair[0]) + abs(best_pair[0]) < abs(contaminated) + abs(solution):
                    best_pair = contaminated, solution

best_pair_list = list(best_pair)
best_pair_list.sort()
print(*best_pair_list)
