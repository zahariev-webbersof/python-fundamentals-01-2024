###### 1. What is the purpose of a Python function?

- A: To store variables
- B: To repeat code multiple times
- C: To organize code into reusable blocks
- D: To perform mathematical calculations

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer ->  C: To organize code into reusable blocks

</p>
</details>

###### 2. What does this Python code snippet calculate?

```javascript
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

print(calculate_average([1, 2, 3, 4, 5]))

```

- A: None
- B: 15
- C: 7.5
- D: 3.0

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 3.0

</p>
</details>

###### 3. What is the purpose of parameters in a function definition?

- A: To specify the return value of the function
- B: To provide input data to the function
- C: To define local variables within the function
- D: To control the execution flow of the function

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: To provide input data to the function

</p>
</details>

###### 4. What happens if a function is called with fewer arguments than specified in its definition?

- A: Python automatically generates additional arguments
- B: Python raises a runtime error
- C: The missing arguments are set to None
- D: The function executes with default values for the missing arguments

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Python raises a TypeError 

</p>
</details>

###### 5. What will be result of this code?

```javascript
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

```

- A: 25
- B: 5
- C: 130
- D: 120

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 120

</p>
</details>

###### 6. What is a recursive function?

- A: A function that calls itself
- B: A function that returns a boolean value
- C: A function that executes in reverse order
- D: A function that iterates over a sequence

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A function that calls itself

</p>
</details>

###### 7. How do you call a function in Python?

- A: By using the call keyword followed by the function name
- B: By using the execute keyword followed by the function name
- C: By using the function name followed by parentheses and any required arguments
- D: By using the run keyword followed by the function name

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: By using the function name followed by parentheses and any required arguments

</p>
</details>

###### 8. What is the purpose of the return statement in a function?

- A: To terminate the function execution
- B: To print output to the console
- C: To specify the function's input parameters
- D: To return a value from the function

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: To return a value from the function

</p>
</details>

###### 9. What is the difference between a function definition and a function call?

- A: A function definition defines the behavior of a function, while a function call executes that behavior.
- B: A function definition executes the behavior of a function, while a function call defines that behavior.
- C: There is no difference; both terms refer to the same action.
- D: A function definition defines input parameters, while a function call provides actual arguments.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A function definition defines the behavior of a function, while a function call executes that behavior.

</p>
</details>

###### 10. 

```javascript
def func(a, b):
    return a ** b

result = func(2, func(2, 2))
print(result)

```

- A: 4
- B: 16
- C: 256
- D: 65536

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 16
</p>
</details>


###### 11. BONUS QUESTION -> What is the output of the following Python code that calculates the base 10 logarithm of 100?

```javascript
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(5)
print(result)

```

- A: 3
- B: 6
- C: 5
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What is the output of the following Python code?

```javascript
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_or_odd(2) == even_or_odd(3))

```

- A: True
- B: False
- C: Error
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 13. 😈 DEVIL QUESTION 😈

```javascript
def func():
    return [lambda x: x * i for i in range(5)]

results = [m(2) for m in func()]
print(results)


```

- A: [8, 8, 8, 8, 8]
- B: [0, 1, 4, 9, 16]
- C: [8, 10, 12, 14, 16]
- D: [0, 2, 4, 6, 8]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 14. 😈 DEVIL QUESTION 😈

```javascript
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        result = func(*args, **kwargs)
        print("After calling function")
        return result
    return wrapper

@my_decorator
def my_function(x):
    return x * 2

result = my_function(5)
print(result)
```

- A: Before calling function After calling function 10
- B: Before calling function 10 After calling function
- C: 10 Before calling function After calling function
- D: Before calling function 10

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
