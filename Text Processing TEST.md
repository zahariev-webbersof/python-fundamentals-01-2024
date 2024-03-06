###### 1. Which string method is used to convert a string to lowercase?

- A: upper()
- B: lower()
- C: capitalize()
- D: swapcase()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> lower()

</p>
</details>

###### 2. What is the output of the following code?

```python
string = "Hello, world!"
print(string[3:7])

```

- A: "lo, "
- B: "lo, w"
- C: "lo,w"
- D: "lo, wo"

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: "lo, "

</p>
</details>

###### 3. What does the strip() method do in Python?

- A: Removes leading and trailing whitespace from a string
- B: Removes all occurrences of a specified character from a string
- C: Splits a string into a list of substrings based on a delimiter
- D: Returns the index of the first occurrence of a substring in a string

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: Removes leading and trailing whitespace from a string

</p>
</details>

###### 4. Which string method can be used to check if a string starts with a specific prefix?

- A: startswith()
- B: endswith()
- C: contains()
- D: find()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: startswith()

</p>
</details>

###### 5. What does the following Python code do?

```python
text = "hello world"
result = " ".join(word[::-1] for word in text.split())
print(result)

```

- A: Reverses the order of words in the text
- B: Reverses each word in the text
- C: Removes whitespace from the text
- D: Converts the text to lowercase

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Reverses each word in the text

</p>
</details>

###### 6. Which slice notation is used to get every other character from a string?

- A: string[::2]
- B: string[1::2]
- C: string[::-1]
- D: string[-1::-1]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: string[::2]

</p>
</details>

###### 7. Which of the following string methods in Python is used to find the index of the first occurrence of a specified substring?

- A: index()
- B: find()
- C: search()
- D: locate()
  
<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: find()

</p>
</details>

###### 8. What does the following slice notation in Python represent: my_string[2:8:2]?

- A: It selects every second character from index 2 to index 8 in my_string
- B: It selects every second character from index 2 to index 7 in my_string
- C: It selects every character from index 2 to index 8 in my_string
- D: It selects every second character from index 2 to index 9 in my_string

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: It selects every second character from index 2 to index 8 in my_string

</p>
</details>

###### 9. Which method in Python is used to concatenate strings?

- A: concat()
- B: merge()
- C: join()
- D: append()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: join()

</p>
</details>

###### 10. What is the output of the following Python code?

```python
text = "hello world"
result = text.find("o")
print(result)

```

- A: 8
- B: 5
- C: 4
- D: 2

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: 4
</p>
</details>


###### 11. BONUS QUESTION -> What does the following Python code do?

```Python
text = "hello"
result = "".join(sorted(set(text)))
print(result)


```

- A: Removes duplicates and sorts the characters in ascending order
- B: Removes duplicates and sorts the characters in descending order
- C: Sorts the characters in descending order without removing duplicates
- D: Sorts the characters in ascending order without removing duplicates

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What will be the output of the following code?

```python
text = "hello world"
result = "".join(text[i] for i in range(len(text)-1, -1, -1))
print(result)
```

- A: Reverses the order of characters in the text
- B: Removes whitespace from the text
- C: Creates a new string with characters from the original string in reverse order
- D: Capitalizes each word in the text

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 13. 😈 DEVIL QUESTION 😈 Consider the following Python code:

```python
text = "hello world"
result = "".join([char.upper() if char.islower() else char.lower() for char in text])
print(result)
```

- A: Reverses the order of characters in the text
- B: Capitalizes each word in the text
- C: Swaps the case of each character in the text
- D: Removes all whitespace characters from the text

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
