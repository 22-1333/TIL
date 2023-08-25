# 4864

"""
# using member operator
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt = 0
    if str1 in str2:
        cnt += 1
    print(f"#{tc} {cnt}")

# not using member operator
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        cnt = 0
        for j in range(len(str1)):
            if str1[j] == str2[i + j]:
                cnt += 1
        if cnt == len(str1):
            result = 1
"""

# 4861

"""
# palindrome
def find_p(n, m, arr):
    for i in range(n):
        for j in range(n - m + 1):
            h = arr[i][j:j + m]
            v = [arr[k][i] for k in range(j, j + m)]

            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    input_arr = [list(input()) for _ in range(N)]
    result = find_p(N, M, input_arr)
    print(f"#{tc}", "".join(result))
"""

# 4865

"""
# with method
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt_list = list()
    
    for i in str1:
        cnt_list.append(str2.count(i))
    result = max(cnt_list)
    print(f"{tc} {result}")
    
# without method
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                 cnt += 1
        if result < cnt:
            result = cnt
    print(f"{tc} {result}") 
"""

# extra_pro_2

"""
# with method
print(eval(input()))

# without method
ex = input()
if ex[0] == "-":
    ex = "0" + ex
word = ex.split("+")
ans = 0
for w in word:
    w = w.split("-")
    inner_ans = int(w[0])
    for i in range(1, len(w)):
        inner_ans -= int(w[i])
    ans += inner_ans
print(ans)
"""

# extra_pro_3

"""
word = input()
result = 0
for i in range(len(word)):
    temp = ""
    index = i + 1
    if word[i] == "[":
        while word[index] != "]":
            temp += word[index]
            index += 1
        result += int(temp)
    elif word[i] == "{":
        while word[index] != "}":
            temp += word[index]
            index += 1
        result *= int(temp)
print(result)
"""

# extra_pro_4

"""
def year_cnt(year):
    a = b = c = d =1
    if year == "XXXX":
        return 1
    if year[0] == "X":
        a = 9
    if year[1] == "X":
        b = 10
    if year[2] == "X":
        c = 10
    if year[3] == "X":
        d = 10
    return a * b * c * d


def month_cnt(month):
    if len(month) == 1:
        if month == "X":
            return 9
    if len(month) == 2:
        if month[1] == "X":
            return 3

    return 1


def day_cnt(day):
    if day == "X":
        return 9
    if day == "XX":
        return 22
    if day[1] == "X":
        if day[0] != "3":
            return 10
        return 2

    return 1


D = input().split(".")
y = year_cnt(D[0])
m = month_cnt(D[1])
d = day_cnt(D[2])
print(y * m * d)
"""
