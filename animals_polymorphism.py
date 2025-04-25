class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def move(self):
        print(f"{self.name} is running happily!")
    
    def speak(self):
        print(f"{self.name} says: Woof! Woof!")


class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming gracefully! ")
    
    def speak(self):
        print(f"{self.name} says: Blub blub...")


class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying high in the sky! ")
    
    def speak(self):
        print(f"{self.name} says: Tweet tweet!")


class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering silently! ")
    
    def speak(self):
        print(f"{self.name} says: Hisssss...")


# Demonstrate polymorphism
def animal_concert(animals):
    for animal in animals:
        animal.move()
        animal.speak()
        print("---")


# Creates a list of different animals
animals = [
    Dog("Buddy"),
    Fish("Nemo"),
    Bird("Sky"),
    Snake("Viper")
]

# Allows the animals move and speak!
animal_concert(animals)