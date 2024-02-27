class Animal:
    instances_count = 0

    def __init__(self):
        Animal.instances_count += 1

    @classmethod
    def count_instances(cls):
        return cls.instances_count

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

print(Animal.count_instances())