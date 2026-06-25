from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Dog(Animal):
    def move(self):
        print("I can Bark")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Lion(Animal):
    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Dog()
K.move()

R = Snake()
R.move()

K = Lion()
K.move()