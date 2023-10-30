#Polymorphisum

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the speak method using polymorphism
print(animal_sound(dog))
print(animal_sound(cat))
