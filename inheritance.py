
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I don't know what I say.")

    def show(self):
        print(f"This is {self.name} and he is {self.age} years old.")

class Cat(Pet): #class Pet() inside the brackets of class Dog() and Cat() helps us use the attributes of Pet() class.
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"This is {self.name} and he is {self.age} years old and he is {self.color}.")

class Dog(Pet): 
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass #It will print 'I don't know what I say' as it refers to the class Pet()

p = Pet("Tommy", 3)
p.speak()
c = Cat("Joe", 1, "Ginger")
c.show()
d = Dog("Jim", 2)
d.speak()
f = Fish("Bubbles", 10)
f.speak()