text = input()

sorted_text = [ch for ch in text if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(sorted_text))