class Animal:
    def __init__(self, name, species, age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
    
    def eat(self):
        print(f"{self.name} the {self.species} is eating.")
    
    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")
    
    def butchering(self):
        print(f"{self.name} the {self.species} is to be butchered.")


class Cow(Animal):
    def __init__(self, name, age, weight, milk):
        super().__init__(name, "Cow", age, weight)
        self.milk = milk
    
    def produce_milk(self):
        print(f"{self.name} the Cow produced {self.milk} liters of milk today.")
    
    def lived(self):
        print(f"{self.name} the Cow is {self.age} years old.")


class Chicken(Animal):
    def __init__(self, name, age, weight, egg):
        super().__init__(name, "Chicken", age, weight)
        self.egg = egg
    
    def produce_egg(self):
        print(f"{self.name} the Chicken produced {self.egg} eggs today.")
    
    def lived(self):
        print(f"{self.name} the Chicken is {self.age} years old.")


class Sheep(Animal):
    def __init__(self, name, age, weight, milk):
        super().__init__(name, "Sheep", age, weight)
        self.milk = milk
    
    def produce_milk(self):
        print(f"{self.name} the Sheep produced {self.milk} liters of milk today.")
    
    def lived(self):
        print(f"{self.name} the Sheep is {self.age} years old.")


def main():
    # Create animals
    cow = Cow("Masha", 5, 500, 10)
    chicken = Chicken("Hen", 2, 4, 3)
    sheep = Sheep("Buck", 3, 80, 2)

    # Perform actions
    cow.eat()
    cow.produce_milk()
    cow.lived()

    chicken.sleep()
    chicken.produce_egg()
    chicken.lived()

    sheep.eat()
    sheep.produce_milk()
    sheep.lived()

    cow.butchering()

main()