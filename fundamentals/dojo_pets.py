class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name,last_name,treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        return print( f"Takes the {self.pet} for a walk to exercice the muscles, afterward {self.first_name} {self.last_name} give it some {self.treats}")
    def feed(self):
        return print( f"Gives the {self.pet} some {self.pet_food}, to strenth the {self.pet} muscle after exercise")
    def bathe(self):
        return print( f"After a long week give the {self.pet} a fresh bath")
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
class Pet:
    def __init__(self, name, type, tricks):
        self.pet_name = name
        self.pet_type = type
        self.pet_tricks = tricks
# implement __init__( name , type , tricks ):
# implement the following methods:

# sleep() - increases the pets energy by 25
    def sleep(self):
        pass
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        pass
# play() - increases the pet's health by 5
    def play(self):
        pass
# noise() - prints out the pet's sound
    def noise(self):
        pass
manolo = Ninja(first_name = 'Manolo',last_name = 'Perez', treats = 'Candy Bones', pet_food = 'Protein Dog Food', pet = 'Dog')
bobby = Pet(name = 'Bobby', type = 'Chiguagua', tricks = 'He uses his sence of smell to find hidden objects')
manolo.walk()
manolo.feed()
manolo.bathe()