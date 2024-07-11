class Dog: # We have created a blueprint for any object that are of type dog.
    def __init__(self, name, age):
        self.name = name #self.name is an attribute to class Dog
        self.age = age
        print(name, age)
    def add_one(self, x):
        return x + 1
    def bark(self): #Method can also be defined as a function within a class.
        print("Bark")

d = Dog("Tim", 2)#Tim refers to the name we gave in the __init__(self, name)
d.bark() #Calling the method bark() on our object d(Dog).
print(d.add_one(4))
print(type(d))
#Output : <class '__main__.Dog'. Underscore defines what module our class was defined in.