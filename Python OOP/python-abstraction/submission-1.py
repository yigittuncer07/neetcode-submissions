class Superhero:
    def __init__(self, name: str):
       self._name = name
       self.__power_level = 40

    def fly(self):
        if self.__power_level >= 20:
            self.__power_level -= 20
            return "Up up and away!"
        return "Too tired to fly..."



# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())  
print(hero.fly())
print(hero.fly())  
