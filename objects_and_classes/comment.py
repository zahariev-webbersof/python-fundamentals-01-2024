class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello, {self.name}!'


person1 = Person('Ivan', 25)
person2 = Person('Gosho', 31)
person3 = Person('Pesho', 44)


print(person1.age)
person1.age += 1
print(person1.age)
