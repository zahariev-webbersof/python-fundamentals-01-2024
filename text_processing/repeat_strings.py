data = input().split()
repeat_text = [text * len(text) for text in data]
print(''.join(repeat_text))