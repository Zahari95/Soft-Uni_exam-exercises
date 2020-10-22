from collections import deque


def check_secondary_colors(result_colors, secondary_colors):
    for color in result_colors:
        if color == "orange":
            if 'red' not in result_colors or 'yellow' not in result_colors:
                result_colors.remove(color)
        elif color == "purple":
            if 'red' not in result_colors or 'blue' not in result_colors:
                result_colors.remove(color)
        elif color == "green":
            if 'yellow' not in result_colors or 'blue' not in result_colors:
                result_colors.remove(color)
    return result_colors


line = deque([x for x in input().split()])

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
result_colors = []

while line:
    if len(line) > 1:
        substring = line.popleft()
        second_substring = line.pop()
        first_comb = substring+second_substring
        second_comb = second_substring+substring
        if first_comb in main_colors or first_comb in secondary_colors:
            result_colors.append(first_comb)
        elif second_comb in main_colors or second_comb in secondary_colors:
            result_colors.append(second_comb)
        else:
            if len(substring) > 1:
                substring = substring[:-1]
                line.insert(len(line) // 2, substring)
            if len(second_substring) > 1:
                second_substring = second_substring[:-1]
                line.insert(len(line) // 2, second_substring)
    elif len(line) == 1:
        substring = line.pop()
        if substring in main_colors or substring in secondary_colors:
            result_colors.append(substring)

result_colors = check_secondary_colors(result_colors, secondary_colors)
print(result_colors)