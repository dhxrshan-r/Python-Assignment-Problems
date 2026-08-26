class pet(object):
    def __init__(self, name, breed, age,energy):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = energy

    def feed(self, amount):
        self.energy += amount

    def print_info(self):
        print("name:", self.name)
        print("breed:", self.breed)
        print("age:", self.age)
        print("energy:", self.energy)
    
class Dog(pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age, energy=5)
    
    def speak(self):
        return "Bark!"
    
    def print_info(self):
        super().print_info()
    
class Cat(pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age, energy=5)

    def speak(self):
        return "Meow"
    
    def print_info(self):
        super().print_info()

d = Dog("Browny", "Siberian Husky", "2 year")
c = Cat("Abby", "Scottish Fold", "1 Year")
d.print_info()
print()
c.print_info()
print()