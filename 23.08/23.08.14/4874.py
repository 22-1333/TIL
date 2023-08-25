T = int(input())

for tc in range(1, T + 1):
    operation_code = list(input().split())
    stack = list()

    for code in operation_code:
        try:
            stack.append(int(code))
        except ValueError:
            if len(stack) >= 2:
                second_number = stack.pop()
                first_number = stack.pop()

                if code == "+":
                    stack.append(int(first_number + second_number))
                elif code == "-":
                    stack.append(int(first_number - second_number))
                elif code == "*":
                    stack.append(int(first_number * second_number))
                elif code == "/":
                    stack.append(int(first_number / second_number))
                else:
                    ans = "error"
                    break
            else:
                if code == ".":
                    ans = stack.pop()
                else:
                    ans = "error"
                    break

    print(f"#{tc} {ans}")
