from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

datura_bomb = 40
cherry_bomb = 60
smoke_bomb = 120

bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

while len(bomb_effects) > 0 and len(bomb_casings) > 0:
    curr_effect = bomb_effects.popleft()
    curr_casing = bomb_casings.pop()

    if curr_effect + curr_casing == datura_bomb:
        bombs['Datura Bombs'] += 1
    elif curr_effect + curr_casing == cherry_bomb:
        bombs['Cherry Bombs'] += 1
    elif curr_effect + curr_casing == smoke_bomb:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_effects.appendleft(curr_effect)
        bomb_casings.append(curr_casing - 5)

    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        break

if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join(map(str, bomb_effects))}')
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f'Bomb Casings: {", ".join(map(str, bomb_casings))}')
else:
    print("Bomb Casings: empty")

for key, value in sorted(bombs.items()):
    print(f'{key}: {value}')
