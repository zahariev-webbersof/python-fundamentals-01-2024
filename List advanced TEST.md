###### 1. What will be the output of the following Python code?

```javascript
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
result = reduce(lambda x, y: x * y, squared)
print(result)

```

- A: 120
- B: 240
- C: 720
- D: 14400

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer ->  D: 14400 - The code squares each number in the list and then multiplies all the squared numbers together using reduce. So, the result is  (2 × 2) * (3 × 3) * (4 × 4) * (5 × 5)  = 14400

</p>
</details>

###### 2. What is the most efficient way to create a set containing the squares of numbers from 1 to 10?

- A: {x**2 for x in range(1, 11)}
- B: set(map(lambda x: x**2, range(1, 11)))
- C: {x: x**2 for x in range(1, 11)}
- D: set([x**2 for x in range(1, 11)])

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: {x**2 for x in range(1, 11)}

</p>
</details>

###### 3. Which of the following statements is true regarding list comprehensions in Python?

- A: List comprehensions can only generate lists of integers.
- B: List comprehensions can include if-else statements for filtering.
- C: List comprehensions cannot be nested within each other.
- D: List comprehensions are slower than traditional for loops for iterating over large datasets.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: List comprehensions can include if-else statements for filtering.

</p>
</details>

###### 4. What does the filter() function do in Python?

- A: It applies a function to each element of an iterable and returns a new iterable.
- B: It creates an iterator that generates elements as long as the given condition is true.
- C: It filters out elements from an iterable based on a given condition.
- D: It reduces the iterable to a single value using the given function.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: It filters out elements from an iterable based on a given condition.

</p>
</details>

###### 5. What does the any() function in Python return?

- A: True if all elements in comprehension are True.
- B: True if any element in an iterable is True.
- C: True if no elements in an iterable are True.
- D: True if the iterable is empty.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: True if any element in an iterable is True.

</p>
</details>

###### 6. What will be result from this code?

```javascript
from functools import reduce
numbers = [2, 3, 4, 5, 6]
product = reduce(lambda x, y: x * y, numbers)

```

- A: Computes the factorial of the last number in the list numbers.
- B: Computes the product of all the numbers in the list numbers.
- C: Computes the sum of all the numbers in the list numbers.
- D: Computes the square of each number in the list numbers.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B) Computes the product of all the numbers in the list numbers.

</p>
</details>

###### 7. Which of the following Python expressions returns the sum of the squares of all even numbers in the list nums?

- A: sum([x**2 for x in nums if x % 2 == 0])
- B: reduce(lambda x, y: x + y**2, filter(lambda x: x % 2 == 0, nums))
- C: reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
- D: sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

</p>
</details>

###### 8. What will be the result of this code? 

```javascript
from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, map(lambda x: x**2, nums))

```

- A: 55
- B: 62
- C: 20
- D: 48

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A) 55

</p>
</details>

###### 9. What is the purpose of the zip() function in Python?

- A: It compresses files into a zip archive.
- B: It merges two or more iterables element-wise into tuples.
- C: It sorts the elements of an iterable in ascending order.
- D: It calculates the dot product of two vectors.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: It merges two or more iterables element-wise into tuples.

</p>
</details>

###### 10. Which of the following Python expressions correctly creates a list containing the lengths of strings from another list words?

- A: [len(word) for word in words]
- B: list(map(len, words))
- C: [word: len(word) for word in words]
- D: [word.len() for word in words]


<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A) [len(word) for word in words]
</p>
</details>


###### 11. BONUS QUESTION -> What is the output of the following Python code?

```javascript
from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, map(lambda x: x**3, filter(lambda x: x % 2 == 0, nums)))
print(result)

```

- A: 64
- B: 72
- C: 88
- D: 86

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What is the output of the following Python code?

```javascript
data = [1, 2, 3, 4, 5]
result = [x**2 if x % 2 == 0 else x**3 for x in data if x > 2]
print(result)

```

- A: [9, 16, 25]
- B: [8, 27, 64, 125]
- C: [27, 16, 125]
- D: [4, 9, 16]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 13. 😈 DEVIL QUESTION 😈

```javascript
def custom_func(x):
    return x if x % 2 == 0 else x**2

data = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, map(custom_func, filter(lambda x: x < 5, data)))

```

- A: 9
- B: 10
- C: 11
- D: 16

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 14. 😈 DEVIL QUESTION 😈

```javascript
from functools import reduce


def custom_func(x):
    return x + 1 if x < 5 else x - 1

data = [1, 2, 3, 4, 5, 6, 7, 8]
result = reduce(lambda x, y: x * y, map(custom_func, filter(lambda x: x % 2 == 0, data)))

print(result)
```

- A: 22
- B: 6
- C: 525
- D: 256

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
