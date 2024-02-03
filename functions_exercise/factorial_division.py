def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_division_function(num1, num2):
    result1 = factorial(num1)
    result2 = factorial(num2)
    division_result = result1 / result2
    return f'{division_result:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial_division_function(first_number, second_number))