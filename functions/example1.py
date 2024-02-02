def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error: Division By Zero!'


def calculator():
    operation = input('Enter the operator (+, -, *, /): ')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print('Error: Invalid operation!')
        return

    print('Result:', result)


calculator()
