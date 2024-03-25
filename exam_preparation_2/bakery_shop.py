stock = {}
sold_count = 0

while True:
    command = input()

    if command == 'Complete':
        break

    action, quantity, food = command.split()
    quantity = int(quantity)

    if action == 'Receive':
        if quantity <= 0:
            continue
        if food not in stock:
            stock[food] = 0
        stock[food] += quantity

    elif action == 'Sell':
        if food not in stock:
            print(f'You do not have any {food}.')
            continue

        if stock[food] >= quantity:
            stock[food] -= quantity
            sold_count += quantity
            print(f'You sold {quantity} {food}.')

            if stock[food] == 0:
                del stock[food]
        else:
            sold_quantity = stock[food]
            sold_count += sold_quantity
            print(f'There aren\'t enough {food}. You sold the last {sold_quantity} of them.')
            del stock[food]

for food, quantity in stock.items():
    print(f'{food}: {quantity}')

print(f'All sold: {sold_count} goods')