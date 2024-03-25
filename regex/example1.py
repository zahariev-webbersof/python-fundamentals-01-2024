import re

text = 'Hello World'
result = re.findall('hello', text, re.I)
print(result)