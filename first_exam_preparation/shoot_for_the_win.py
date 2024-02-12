def reduce_values(target_list, index):
    special_value = target_list[index]
    target_list[index] = -1

    for i in range(len(target_list)):
        if target_list[i] == -1:
            continue

        if special_value < target_list[i]:
            target_list[i] -= special_value
        else:
            target_list[i] += special_value

    return target_list


def shot_for_the_win(target_sequence):
    count_of_shot_targets = 0

    while True:
        command = input()

        if command == 'End':
            break

        index = int(command)

        if 0 <= index < len(target_sequence) and target_sequence[index] != -1:
            count_of_shot_targets += 1
            reduce_values(target_sequence, index)

    convert_target_values_to_string = [str(num) for num in target_sequence]
    print(f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_target_values_to_string)}")
    

data = list(map(int, input().split()))
shot_for_the_win(data)