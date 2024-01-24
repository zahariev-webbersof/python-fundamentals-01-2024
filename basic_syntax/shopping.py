budget = int(input())
total_price = 0

while True:
    command = input()

    if command == 'End':
        print("You bought everything needed.")
        break

    price = int(command)

    if total_price + price > budget:
        print("You went in overdraft!")
        break

    total_price += price

