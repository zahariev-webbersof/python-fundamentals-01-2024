def is_perfect_number(number):
    divisors_sum = 0

    for divisior in range(1, number):
        if number % divisior == 0:
            divisors_sum += divisior

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(is_perfect_number(num))