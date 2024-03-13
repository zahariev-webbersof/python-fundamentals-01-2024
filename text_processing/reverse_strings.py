while True:
    word = input()

    if word == 'end':
        break

    print(f'{word} = {word[::-1]}')