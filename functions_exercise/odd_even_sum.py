def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_even_sum(number))