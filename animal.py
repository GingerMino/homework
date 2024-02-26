class Animal:
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        print("Woof")

class Cat(Animal):
    def voice(self):
        print("Meow")

class Pig(Animal):
    def voice(self):
        print("Oink")

dog = Dog()
cat = Cat()
pig = Pig()

dog.voice()
cat.voice()
pig.voice()