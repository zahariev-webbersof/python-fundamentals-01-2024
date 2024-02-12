def sort_names():
    names = input().split(', ')
    sorted_names = sorted(names, key=lambda name: (-len(name), name))

    return sorted_names


result = sort_names()
print(result)
