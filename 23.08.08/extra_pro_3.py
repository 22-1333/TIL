string = input()
braces = 0
brackets = 0
number = 0
result = 0

for idx in range(len(string)):
    if string[idx] == "{":
        braces = idx + 1
    elif string[idx] == "}":
        result = result * int(string[braces:idx])
    elif string[idx] == "[":
        brackets = idx + 1
    elif string[idx] == "]":
        result = result + int(string[brackets:idx])
    print(result)

print(result)
