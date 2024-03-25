username = input()


while True:
    command = input().split()
    current_command = command[0]

    if current_command == 'Registration':
        break

    if current_command == 'Letters':
        case = command[1]

        if case == 'Lower':
            username = username.lower()
        elif case == 'Upper':
            username = username.upper()

        print(username)

    elif current_command == 'Reverse':
        start_index, end_index = int(command[1]), int(command[2])

        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            reversed_substring = username[start_index:end_index + 1][::-1]
            print(reversed_substring)

    elif current_command == 'Substring':
        substring = command[1]

        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif current_command == 'Replace':
        char = command[1]
        username = username.replace(char, '-')
        print(username)

    elif current_command == 'IsValid':
        char = command[1]

        if char in username:
            print('Valid username.')
        else:
            print(f'{char} must be contained in your username.')