def is_valid(row, col):  # check for valid move of santa
    return 0 <= row <= n and 0 <= col <= n


def move(neighbourhood, santa_position, row, col, happy_nice_kids, presents):  # move santa on desire cell
    neighbourhood[santa_position[0]][santa_position[1]] = '-'
    if neighbourhood[row][col] == 'V':
        presents -= 1
        happy_nice_kids += 1
    elif neighbourhood[row][col] == 'C':
        if neighbourhood[row - 1][col] == 'V':
            neighbourhood[row - 1][col] = '-'
            presents -= 1
            happy_nice_kids += 1
        elif neighbourhood[row - 1][col] == 'X':
            neighbourhood[row - 1][col] = '-'
            presents -= 1
        if neighbourhood[row + 1][col] == 'V':
            neighbourhood[row + 1][col] = '-'
            presents -= 1
            happy_nice_kids += 1
        elif neighbourhood[row + 1][col] == 'X':
            neighbourhood[row + 1][col] = '-'
            presents -= 1
        if neighbourhood[row][col - 1] == 'V':
            neighbourhood[row][col - 1] = '-'
            presents -= 1
            happy_nice_kids += 1
        elif neighbourhood[row][col - 1] == 'X':
            neighbourhood[row][col - 1] = '-'
            presents -= 1
        if neighbourhood[row][col + 1] == 'V':
            neighbourhood[row][col + 1] = '-'
            presents -= 1
            happy_nice_kids += 1
        elif neighbourhood[row][col + 1] == 'X':
            neighbourhood[row][col + 1] = '-'
            presents -= 1
    neighbourhood[row][col] = 'S'
    santa_position = (row, col)
    return santa_position, happy_nice_kids, presents


m = int(input())  # count of presents
n = int(input())  # size of the neighbourhood

neighbourhood = []
nice_kids = 0
happy_nice_kids = 0

for i in range(n):  # create the neighbourhood and check for santa position and nice_kids
    line = input().split()
    for j in range(n):
        if line[j] == 'S':
            santa_position = (i, j)
        elif line[j] == 'V':
            nice_kids += 1
    neighbourhood.append(line)

command = input()

while command != 'Christmas morning':
    if command == 'up':
        row = santa_position[0] - 1
        col = santa_position[1]
        if is_valid(row, col):
            santa_position, happy_nice_kids, m = move(neighbourhood, santa_position, row, col, happy_nice_kids, m)
    elif command == 'down':
        row = santa_position[0] + 1
        col = santa_position[1]
        if is_valid(row, col):
            santa_position, happy_nice_kids, m = move(neighbourhood, santa_position, row, col, happy_nice_kids, m)
    elif command == 'left':
        row = santa_position[0]
        col = santa_position[1] - 1
        if is_valid(row, col):
            santa_position, happy_nice_kids, m = move(neighbourhood, santa_position, row, col, happy_nice_kids, m)
    elif command == 'right':
        row = santa_position[0]
        col = santa_position[1] + 1
        if is_valid(row, col):
            santa_position, happy_nice_kids, m = move(neighbourhood, santa_position, row, col, happy_nice_kids, m)
    if m <= 0:
        break
    command = input()

if m <= 0 < (nice_kids - happy_nice_kids):
    print("Santa ran out of presents!")

[print(" ".join(row)) for row in neighbourhood]

if happy_nice_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - happy_nice_kids} nice kid/s.")
