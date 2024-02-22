from calculator import Calculator


def main():
    calc = Calculator()

    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    print("Addition:", calc.add(num1, num2))
    print("Subtraction:", calc.subtract(num1, num2))
    print("Multiplication:", calc.multiply(num1, num2))
    print("Division:", calc.divide(num1, num2))


if __name__ == '__main__':
    main()