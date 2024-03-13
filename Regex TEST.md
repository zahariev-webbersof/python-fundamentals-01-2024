
![featured](https://github.com/zahariev-webbersof/python-fundamentals-01-2024/assets/68993494/8cea92b4-0b7a-4c89-863e-955e1f681e44)


###### 1. What is the purpose of the re.match() function in Python's re module?

- A: To search for a pattern anywhere in a string
- B: To search for a pattern only at the beginning of a string
- C: To search for a pattern case-insensitively
- D: To search for a pattern in multiple strings simultaneously

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: To search for a pattern only at the beginning of a string

</p>
</details>

###### 2. What Python code snippet correctly checks if a string contains any whitespace character using regular expressions?

```python
import re

text = "Hello World"
pattern = ????
result = re.search(pattern, text)
if result:
    print("String contains whitespace character")
else:
    print("String does not contain whitespace character")

```

- A: pattern = r'\S'
- B: pattern = r'\s'
- C: pattern = r'\w'
- D: pattern = r'\W'

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: pattern = r'\s'

</p>
</details>

###### 3. Which metacharacter in regular expressions matches any single character?

- A: .
- B: *
- C: +
- D: ?

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: .

</p>
</details>

###### 4. What does the re.findall() function return in Python's re module?

- A: The first occurrence of a pattern in a string
- B: All occurrences of a pattern in a string as a list
- C: The index of the first occurrence of a pattern in a string
- D: The count of occurrences of a pattern in a string

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: All occurrences of a pattern in a string as a list

</p>
</details>

###### 5. What Python code snippet correctly substitutes all occurrences of "apple" with "banana" in a string using regular expressions?

```python
import re

text = "I like apple pie and apple juice"
pattern = r'apple'
replaced_text = re.sub(pattern, 'banana', text)
print(replaced_text)

```

- A: pattern = r'apple'
- B: pattern = r'banana'
- C: pattern = r'apple$'
- D: pattern = r'^banana'

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: pattern = r'apple'

</p>
</details>

###### 6. Which quantifier matches zero or one occurrence of the preceding character or group?

- A: +
- B: *
- C: ?
- D: {}

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: ?

</p>
</details>

###### 7. Which anchor in regular expressions matches the beginning of a line?

- A: ^
- B: $
- C: %
- D: &
  
<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: ^

</p>
</details>

###### 8. What does the re.search() function do in Python's re module?

- A: Searches for a pattern only at the beginning of a string
- B: Searches for a pattern anywhere in a string
- C: Searches for a pattern case-insensitively
- D: Searches for a pattern in multiple strings simultaneously

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Searches for a pattern anywhere in a string

</p>
</details>

###### 9. What does the re.compile() function do in Python's re module?

- A: Compiles a regular expression pattern into a regular expression object
- B: Compiles a string into a regular expression pattern
- C: Compresses a string
- D: Compares two regular expression patterns

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: Compiles a regular expression pattern into a regular expression object

</p>
</details>

###### 10. What Python code snippet correctly finds all words that start with the letter "a" or "b" using regular expressions?

```python
import re

text = "apple banana cat dog"
pattern = r'\b[a-b]\w+'
result = re.findall(pattern, text)
print(result)


```

- A: pattern = r'\ba-b\w+'
- B: pattern = r'\b[a-b]\w+'
- C: pattern = r'\b[a|b]\w+'
- D: pattern = r'\b[a-b]+\w+'

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: pattern = r'\b[a-b]\w+'
</p>
</details>


###### 11. 😈 DEVIL QUESTION 😈 What Python code snippet correctly replaces all occurrences of numbers within angle brackets with the word "NUMBER" using regular expressions?

```python
import re

text = "<123> is less than <456> and <789> is greater"
pattern = ???
replaced_text = re.sub(pattern, 'NUMBER', text)
print(replaced_text)

```

- A: pattern = r'<\d+>'
- B: pattern = r'<\d+?>'
- C: pattern = r'<\d*>'
- D: pattern = r'<\d*?>'

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 12. 😈 DEVIL QUESTION 😈 What Python code snippet correctly extracts all email addresses from a given text using regular expressions?

```python
import re

text = "Send email to john@example.com and jane.doe@example.co.uk"
pattern = ?????
matches = re.findall(pattern, text)
print(matches)

```

- A: pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
- B: pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b'
- C: pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b'
- D: pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,6}\b'

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
