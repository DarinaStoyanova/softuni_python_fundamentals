class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species:str, name:str):
        Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self,species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

name_of_the_zoo = input()
number_of_animals = int(input())
zoo = Zoo(name_of_the_zoo)
while True:
    if number_of_animals == 0:
        animal_info = input()
        species_ = animal_info
        print(zoo.get_info(species_))
        break
    else:
        animal_info = input().split(" ")
        type_of_animal = animal_info[0]
        name_of_animal = animal_info[1]
        zoo.add_animal(type_of_animal,name_of_animal)
        number_of_animals -= 1

