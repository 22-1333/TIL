N = int(input())
expression = list(input())
numbers = ["number" for number in range(10)]
space = ((N + 1) // 2)
visited = [0] * space
max_result = 0 - (2 ** 31)


def calculator(left, operator, right):
    if operator == "+":
        return int(left) + int(right)
    elif operator == "*":
        return int(left) * int(right)
    elif operator == "-":
        return int(left) - int(right)


def calculation(parenthesis_list):
    global max_result
    queue = list()

    idx = 0
    while idx < space:
        if parenthesis_list[idx]:
            queue.append(calculator(expression[idx * 2], expression[idx * 2 + 1], expression[idx * 2 + 2]))
            if idx != space - 2:
                queue.append(expression[idx * 2 + 3])
            idx += 2
        else:
            queue.append(expression[idx * 2])
            if idx != space - 1:
                queue.append(expression[idx * 2 + 1])
            idx += 1

    if len(queue) == 1:
        max_result = queue.pop(0)
    else:
        one = queue.pop(0)
        two = queue.pop(0)
        three = queue.pop(0)

        result = calculator(one, two, three)

        while queue:
            second = queue.pop(0)
            third = queue.pop(0)

            result = calculator(result, second, third)

        max_result = max(max_result, result)


def add_parenthesis(n):
    if n >= space - 1:
        calculation(visited)
        return

    visited[n] = 1
    visited[n + 1] = 1
    add_parenthesis(n + 2)
    visited[n] = 0
    visited[n + 1] = 0
    add_parenthesis(n + 1)


add_parenthesis(0)
print(max_result)
