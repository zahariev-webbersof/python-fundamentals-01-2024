banned_words_list = input().split(', ')
text = input()

for banned_word in banned_words_list:
    text = text.replace(banned_word, "*" * len(banned_word))

print(text)