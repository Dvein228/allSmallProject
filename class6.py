from itertools import chain


class Character:
    def __init__(self, name, level):
        self.name=name
        self.level=level

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)

class Warior(Character):
    def __init__(self,name,level,strenght):
        self.name = name
        self.level = level
        self.strenght = strenght

class Mage(Character):
    def __init__(self,name,level,Magic):
        self.name= name
        self.level= level
        self.Magic =Magic
maga = Mage("Мага","5","темная")
Warvara = Warior("Варя","7","большая")