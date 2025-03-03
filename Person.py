class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def that_tells_my_name(self):
        return f'{self.name} is {self.age} years old'
name = input("What is your name?")
age = int(input("What is your age?"))
person = Person(name, age)
print(person.that_tells_my_name())

