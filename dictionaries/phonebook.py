def fill_phonebook():
    phonebook = {}

    while True:
        entry = input().split('-')

        if len(entry) == 1:
            return phonebook, int(entry[0])

        name, number = entry
        phonebook[name] = number


def search_contact(phonebook, name):
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')


def main():
    phonebook, number = fill_phonebook()

    for _ in range(number):
        search_name = input()
        search_contact(phonebook, search_name)


if __name__ == '__main__':
    main()
