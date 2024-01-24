i = 0

while i < 10:
    i += 1

    if i == 3:
        print('Skipping iteration', i)
        continue

    if i == 9:
        print('Breaking loop at iteration', i)
        break

    print('Iteration', i)