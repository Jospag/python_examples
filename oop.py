class Dog:
    def __init__(self, name, age):
        species = "Canis familiaris"
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {self.sound}"

