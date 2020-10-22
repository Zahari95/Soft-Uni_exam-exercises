def is_valid(row, col):  # check for valid move of bunny in desire direction
    return 0 <= row <= n - 1 and 0 <= col <= n - 1


n = int(input())  # size of the field
field = []
max_eggs = -999999999999999
curr_eggs = 0
best_direction = ""
directions = {
              'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }
egg_positions = {
              'up': [],
              'down': [],
              'left': [],
              'right': []
              }

for i in range(n):  # create the matrix (field)
    line = input().split()
    for j in range(n):
        if line[j] == 'B':
            bunny_pos = (i, j)
    field.append(line)

for key, value in directions.items():
    new_row = bunny_pos[0] + (value[0])
    new_col = bunny_pos[1] + (value[1])
    while is_valid(new_row, new_col):
        if field[new_row][new_col].isdigit():
            curr_eggs += int(field[new_row][new_col])
            egg_positions[key].append([new_row, new_col])
            if curr_eggs > max_eggs:
                max_eggs = curr_eggs
                best_direction = key
        else:
            curr_eggs = 0
            break
        new_row += value[0]
        new_col += value[1]
    curr_eggs = 0

print(best_direction)
[print(x) for x in egg_positions[best_direction]]
print(max_eggs)
