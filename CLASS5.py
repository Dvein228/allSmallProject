
class Weapon:
    def __init__(self, name, damage):
        self.name=name
        self.damage=damage

    def info(self):
        print("Ім'я:", self.name)
        print("Урон:", self.damage)

class Character:
    def __init__(self, name, level,weapon):
        self.name=name
        self.level=level
        self.weapon = weapon

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)

Bow= Weapon("лук","1")
Axe= Weapon("Акс","375")

LDFGFDGFDGD=Character("Гном-перегном","5",Bow)
drugoi = Character("Гном","7",Bow)
EsheDrugoi = Character("НеГном","1",Axe)