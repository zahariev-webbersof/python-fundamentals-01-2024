###### 1. What is the primary purpose of dictionaries in Python?

- A: Storing only integers
- B: Storing only strings
- C: Storing key-value pairs
- D: Storing string-numbers pairs
- 
<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Storing key-value pairs

</p>
</details>

###### 2. What is the output of the following code snippet?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('d'))

```

- A: 0
- B: KeyError
- C: None
- D: 3

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: None

</p>
</details>

###### 3. Which method is used to remove a key-value pair from a dictionary by specifying the key?

- A: remove()
- B: pop()
- C: delete()
- D: discard()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: pop()

</p>
</details>

###### 4. In Python, can a dictionary have multiple values for the same key?

- A: No, each key must have a unique value
- B: Yes, but it's not recommended
- C: No, only the last assigned value is stored for a key
- D: Yes, dictionaries can have multiple values for the same key

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: Yes, dictionaries can have multiple values for the same key

</p>
</details>

###### 5. 

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'d': 4, 'e': 5})
print(my_dict)

```

- A: {'a': 1, 'b': 2, 'c': 3}
- B: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
- C: {'d': 4, 'e': 5}
- D: {'d': 4, 'e': 5, 'a': 1, 'b': 2, 'c': 3}

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

</p>
</details>

###### 6. How do you check if a key exists in a dictionary?

- A: exist()
- B: has_key()
- C: contains()
- D: in

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: in

</p>
</details>

###### 7. How do you add a new key-value pair to an existing dictionary in Python?

- A: Using the append() method
- B: Using the add() method
- C: Using the insert() method
- D: By directly assigning a value to a new key
  
<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: By directly assigning a value to a new key

</p>
</details>

###### 8. What is the correct way to iterate over all key-value pairs in a dictionary in Python?

- A: Using a for loop with range(len())
- B: Using a for loop with enumerate()
- C: Using a for loop with items()
- D: Using a while loop with iteritems()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Using a for loop with items()

</p>
</details>

###### 9. Which method is used to get a list of all values in a dictionary?

- A: values()
- B: list_values()
- C: get_values()
- D: retrieve_values()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: values()

</p>
</details>

###### 10. 

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.setdefault('d')
print(my_dict)

```

- A: None
- B: {'a': 1, 'b': 2, 'c': 3, 'd': None}
- C: KeyError
- D: ValueError

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: {'a': 1, 'b': 2, 'c': 3, 'd': None}
</p>
</details>


###### 11. BONUS QUESTION -> What is the time complexity of the popitem() method in Python dictionaries?

- A: O(1)
- B: O(log n)
- C: O(n)
- D: The time complexity varies depending on the implementation

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What will be the output of the following code?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = my_dict.pop('b')
print(my_dict)
```

- A: {'a': 1, 'c': 3, 'b': 2}
- B: TypeError
- C: KeyError
- D: {'a': 1, 'c': 3, 'd': 2}

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 13. 😈 DEVIL QUESTION 😈 What will be the output of the following code?

```python
my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
new_dict = {}
for key, value in my_dict.items():
    new_dict[key] = sum(value)
```

- A: {'a': 6, 'b': 15, 'c': 24}
- B: {'a': 1, 'b': 4, 'c': 7}
- C: {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
- D: {'a': 6, 'b': 15, 'c': 24}

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 14. 😈 DEVIL QUESTION 😈 What will be the output of the following code?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {}
for key, value in my_dict.items():
    if value % 2 == 0:
        new_dict.setdefault('even', []).append(key)
    else:
        new_dict.setdefault('odd', []).append(key)

print(new_dict)
```

- A: {'odd': ['a', 'c'], 'even': ['b']}
- B: {'even': ['b'], 'odd': ['a', 'c']}
- C: {'even': ['b', 'c'], 'odd': ['a']}
- D: {'even': ['b', 'c'], 'odd': ['b']}

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
