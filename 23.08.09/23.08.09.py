# stack

"""
stack = [0] * 10
top = -1

top += 1  # push(1)
stack[top] = 1
top += 1  # push(2)
stack[top] = 2
top += 1  # push(3)
stack[top] = 3
print(stack[top])  # pop()
top -= 1
top -= 1
print(stack[top + 1])
"""

# extra_pro_1

"""
arr = ["3", "5", "1", "9", "7"]
T = [input() for _ in range(4)]


def right(r_lst):
    for i in range(4):
        lst.append(r_lst[i])
    for _ in range(4):
        r_lst.pop(0)


def left(l_lst):
    lst.append(l_lst[0])
    lst.pop(0)


for idx in range(4):
    if T[idx] == "R":
        right(arr)
    if T[idx] == "L":
        left(arr)

print(*arr)
"""

# extra_pro_3

"""
N = int(input())


def solve(num, cnt):
    if num == 1:
        print(cnt)
        return 
    if num % 2 == 0:
        solve(num / 2, cnt + 1)
    else:
        solve(num * 3 + 1, cnt + 1)
        

solve(N, 0)
"""

# extra_pro_4

"""
N = int(input())


def func(num):
    if num // 10 == 0:
        return num
    
    return func(num // 10) + num % 10


result = func(N)
print(result)
"""

# extra_pro_5

"""
card = list(input())
path = [0] * 4
cnt = 0


def card_cnt(level):
    global cnt
    if level == 4:
        cnt += 1
        return

    for i in range(5):
        path[level] = card[i]
        if abs(int(path[level]) - int(path[level - 1])) >= 4:
            continue
        card_cnt(level + 1)


card_cnt(0)
print(cnt)
"""
