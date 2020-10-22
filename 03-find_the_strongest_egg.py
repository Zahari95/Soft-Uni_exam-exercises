def find_strongest_eggs(*args):
    n = args[1]
    sub_list = []
    strongest_eggs = []
    for i in range(n):
        sub_list.append([])
        for j in range(i, len(args[0]), n):
            sub_list[i].append(args[0][j])
    for i in range(n):
        strong = False
        for j in range(len(sub_list[i]) // 2):
            left_egg = sub_list[i][(len(sub_list[i]) // 2) - j - 1]
            middle_egg = sub_list[i][len(sub_list[i]) // 2]
            right_egg = sub_list[i][(len(sub_list[i]) // 2) + j + 1]
            if left_egg < middle_egg > right_egg:
                if right_egg > left_egg:
                    strong = True
                else:
                    strong = False
            else:
                strong = False
        if strong:
            strongest_eggs.append(middle_egg)
    return strongest_eggs


test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))

test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
