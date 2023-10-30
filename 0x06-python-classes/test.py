'''
what is a class ?
- A template for creating an object
- Sets the ground rules for object creation
- Consists of attributes and methods
- Constructor or blue print for creating objects
- User defined Datatypes
What is an Object?
- An instance of a class:
    1. A child created from a parent(template=class)
    2. A version of a class
    3. A specific state of the class
    4. There can be many instances, versions, states of the class
What is a class variable and an object variable?
- Object Variables:
    1. They are specific to the object
    2. Meaning variable scope is only for the istantiated object
What are methods?
- Defines the functionality of an object i.e what can the object do?

Features, fields, properties, attributes
Protected, Private and Public
'''

class Person:

    def __init__(self, name="", age="", color="", school=""):
        self.name = name
        self.age = age
        self.color = color
        self.school = school

    def __str__(self):
        return self.__name + str(self.age)


    def say_my_name(self, age):
        print(f"My name is {self.name} and I am {age} years old")

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name


person1 = Person("ifiok", 10)
print(person1)
