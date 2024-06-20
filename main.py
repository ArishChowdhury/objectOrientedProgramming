class Person:
    # defining a constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("arish",14)
print(p1.name)
print(p1.age)

class Fruit:
    type = "food"
    def fruitmethod(self):
        print("This is a type of fruit accessed through object")

apple = Fruit()
apple.fruitmethod()
print(apple.type)