def calculate_order_price(prices):
    price_without_taxes = sum(prices)
    taxes = sum(price * 0.20 for price in prices)
    return price_without_taxes, taxes


def computer_store():
    prices = []
    additional_discount = False

    while True:
        command = input()

        if command == 'special' or command == 'regular':
            if not prices:
                return "Invalid order!"

            additional_discount = True if command == 'special' else False
            break

        current_price = float(command)

        if current_price < 0:
            print("Invalid price!")
            continue

        prices.append(current_price)

    price_without_taxes, taxes = calculate_order_price(prices)

    if additional_discount:
        total_price = price_without_taxes + taxes
        total_price *= 0.90
        return total_price, price_without_taxes, taxes

    return price_without_taxes + taxes, price_without_taxes, taxes


def print_receipt(total_price, price_without_additional_taxes, taxes):
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_additional_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")


result = computer_store()

if isinstance(result, tuple):
    print_receipt(*result)
else:
    print(result)



