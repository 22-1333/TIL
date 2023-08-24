T = int(input())
for tc in range(1, T + 1):
    string = input()
    word = string[0]
    for idx in range(1, len(string)):
        if word[0] == string[idx]:
            for word_idx in range(1, len(word)):
                if word[word_idx] == string[idx + word_idx]:
                    continue
                else:
                    break
            else:
                print(f"#{tc} {len(word)}")
                break

        word += string[idx]
