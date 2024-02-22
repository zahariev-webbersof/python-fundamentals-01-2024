###### 1. What is the purpose of the __init__ method in a Python class?

- A: To create a new object of the class
- B: To initialize attributes of an object when it is created
- C: To define methods for the class
- D: To destroy an object when it is no longer needed

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: To initialize attributes of an object when it is created

</p>
</details>

###### 2. What is the correct way to create an instance of the Rectangle class with length 5 and width 3?

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

```

- A: rect = Rectangle(length=5, width=3)
- B: rect = Rectangle([5, 3])
- C: rect = Rectangle(length=3, width=5)
- D: rect = Rectangle()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: rect = Rectangle(length=5, width=3)

</p>
</details>

###### 3. Which of the following best describes inheritance in OOP?

- A: The process of creating multiple instances of a class
- B: The ability to reuse code and extend functionality of an existing class
- C: The process of encapsulating data and methods into a single unit
- D: The ability to access attributes and methods of another class

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: The ability to reuse code and extend functionality of an existing class

</p>
</details>

###### 4. What is the term for the process of creating an object from a class?

- A: Inheritance
- B: Abstraction
- C: Encapsulation
- D: Instantiation

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: Instantiation

</p>
</details>

###### 5. How can you access the circumference of a Circle instance named "my_circle" with radius 4?

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

```

- A: my_circle.calculate_circumference()
- B: Circle.calculate_circumference(my_circle)
- C: my_circle.radius
- D: Circle(4).calculate_circumference()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: my_circle.calculate_circumference()

</p>
</details>

###### 6. What is method overriding in OOP?

- A: Creating multiple methods with the same name but different parameters
- B: Redefining a method in the child class with the same name as in the parent class
- C: Calling a method from within another method of the same class
- D: Assigning a new value to an existing attribute of an object

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Redefining a method in the child class with the same name as in the parent class

</p>
</details>

###### 7. What is a class in OOP?

- A: A blueprint for creating objects
- B: A function that initializes the object's attributes
- C: A variable that holds data
- D: A loop that iterates over a sequence
  
<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A blueprint for creating objects

</p>
</details>

###### 8. What does the term "instance" refer to in OOP?

- A: A variable that holds data
- B: A specific realization of a class
- C: A variable that initializes the object's attributes
- D: A blueprint for creating classes

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: A specific realization of a class

</p>
</details>

###### 9. What is the difference between a class and an object in OOP?

- A: A class is a blueprint for creating objects, while an object is an instance of a class
- B: A class is an instance of an object, while an object is a blueprint for creating classes
- C: A class represents behavior, while an object represents data
- D: A class is a static entity, while an object is a dynamic entity

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: A class is a blueprint for creating objects, while an object is an instance of a class

</p>
</details>

###### 10. What will be the output of calling the make_sound() method on a Dog instance?

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

```

- A: None
- B: "Meow!"
- C: "Woof!"
- D: Error

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: "Woof!"
</p>
</details>


###### 11. BONUS QUESTION -> What is the purpose of using a double underscore (__) before the balance attribute in the BankAccount class?

```Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

```

- A: To make the balance attribute public
- B: To make the balance attribute private
- C: To make the balance attribute protected
- D: To make the balance attribute accessible only within the same module

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What will be the output of the following code?

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

account = BankAccount(1000)
account.deposit(500)
print(account.withdraw(2000))

```

- A: 500
- B: "Insufficient funds"
- C: 2000
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 13. 😈 DEVIL QUESTION 😈 What is the purpose of using a property decorator for the name attribute in the Student class?

```python
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string")
```

- A: It restricts access to the name attribute from outside the class.
- B: It allows validation and modification of the name attribute when accessed.
- C: It converts the name attribute into a class-level variable.
- D: It automatically initializes the name attribute with a default value.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>

###### 14. 😈 DEVIL QUESTION 😈 Which class serves as the abstract base class (ABC) in the provided code snippet?

```python
import abc

class Shape(abc.ABC):
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @abc.abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def area(self):
        return 3.14 * self._radius ** 2

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def area(self):
        return self._length * self._width

```

- A: Shape
- B: Circle
- C: Rectangle
- D: abc.ABC

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
