T = int(input())
for tc in range(1, T + 1):
    text = input()
    stack = []
    not_quote = True
    for i in text:
        if i == "'":
            not_quote = not not_quote
        if not_quote:
            if i == "(" or i == "{":
                stack.append(i)
            elif stack and i == ")" and stack[-1] == "(":
                stack.pop(-1)
            elif stack and i == "}" and stack[-1] == "{":
                stack.pop(-1)
            elif i == "}" or i == ")":
                stack.append(i)

    if stack:
        result = 0
    else:
        result = 1

    print(f"#{tc} {result}")
