moving_targets = list(map(int, input().split(" ")))
commands_line = input()

while commands_line != "End":
    commands = commands_line.split(" ")
    command = commands[0]
    if command == "Shoot":
        index = int(commands[1])
        power = int(commands[2])
        if 0 <= index < len(list(map(str, moving_targets))):
            moving_targets[index] -= power
            if moving_targets[index] <= 0:
                moving_targets.pop(index)

    elif command == "Add":
        index = int(commands[1])
        value = int(commands[2])

        if index < 0 or index >= len(moving_targets):
            print("Invalid placement!")
        else:
            moving_targets.insert(index, value)

    elif command == "Strike":
        index = int(commands[1])
        radius = int(commands[2])
        left_border = index - radius
        right_border = index + radius + 1
        if left_border < 0 or right_border >= len(moving_targets):
            print("Strike missed!")
        else:
            for i in range(left_border, right_border):
                del moving_targets[left_border]

    commands_line = input()

print("|".join(list(map(str, moving_targets))))
