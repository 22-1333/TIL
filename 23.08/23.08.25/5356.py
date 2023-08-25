T = int(input())
for tc in range(1, T + 1):
    word_list = list()
    max_len = 0

    for _ in range(5):
        word = list(input())
        max_len = max(max_len, len(word))
        word_list.append(word)

    reading = ""

    for idx in range(max_len):
        for word_number in range(5):
            try:
                reading += word_list[word_number][idx]
            except IndexError:
                continue

    print(f"#{tc} {reading}")
