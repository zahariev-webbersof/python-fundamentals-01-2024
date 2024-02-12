initial_list = input().split('!')

while True:
    command = input()

    if command == "Go Shopping!":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == 'Urgent':
        item = command_parts[1]

        if item not in initial_list:
            initial_list.insert(0, item)

    elif action == 'Unnecessary':
        item = command_parts[1]

        if item in initial_list:
            initial_list.remove(item)

    elif action == 'Correct':
        old_item = command_parts[1]
        new_item = command_parts[2]

        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif action == 'Rearrange':
        item = command_parts[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(', '.join(initial_list))