# products = {}
#
# while True:
#     command = input()
#
#     if command == 'buy':
#         break
#
#     name, price, quantity = command.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in products:
#         products[name] = {'price': price, 'quantity': quantity}
#     else:
#         products[name]['quantity'] += quantity
#
#         if products[name]['price'] != price:
#             products[name]['price'] = price
#
#
# for name, info in products.items():
#     total_price = info['price'] * info['quantity']
#     print(f'{name} -> {total_price:.2f}')


class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

    def update_price(self, price):
        if self.price != price:
            self.price = price



products = {}

while True:
    command = input()

    if command == 'buy':
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = Product(price, quantity)
    else:
        products[name].update_quantity(quantity)
        products[name].update_price(price)


for name, product in products.items():
    total_price = product.price * product.quantity
    print(f'{name} -> {total_price:.2f}')