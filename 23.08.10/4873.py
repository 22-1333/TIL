T = int(input())
for tc in range(1, T + 1):
    string = list(input())
    while True:
        for string_idx in range(len(string)):
            if string_idx < len(string) - 1:
                if string[string_idx] == string[string_idx + 1]:
                    string.pop(string_idx)
                    string.pop(string_idx)
                    break
        else:
            break

    print(f"#{tc} {len(string)}")
