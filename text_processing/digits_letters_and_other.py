text = input()
numbers = ''
letters = ''
characters = ''

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        characters += char

print(numbers)
print(letters)
print(characters)