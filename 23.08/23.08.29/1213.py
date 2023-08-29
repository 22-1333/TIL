for tc in range(10):
    N = int(input())
    vertex_dict = dict()
    for _ in range(N):
        vertex_info = list(input().split())
        vertex_number = vertex_info.pop(0)
        vertex_dict[vertex_number] = vertex_info
    word = ""

    def inorder(num):
        global word
        if len(vertex_dict[num]) == 3:
            inorder(vertex_dict[num][1])
            word += vertex_dict[num][0]
            inorder(vertex_dict[num][2])
        elif len(vertex_dict[num]) == 2:
            inorder(vertex_dict[num][1])
            word += vertex_dict[num][0]
        elif len(vertex_dict[num]) == 1:
            word += vertex_dict[num][0]


    inorder("1")
    print(f"#{tc} {word}")
