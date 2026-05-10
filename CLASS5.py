class Enemy:
    def __init__(self, name, health):
        self.name=name
        self.health=health

    def info(self):
        print("Ім'я:", self.name)
        print("ХП:", self.health)

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
        print(f"Використовує {self.weapon.name} з {self.weapon.damage} урона ")

Bow= Weapon("лук","1")
Axe= Weapon("Акс","375")

LDFGFDGFDGD=Character("Гном-перегном","5",Bow)
drugoi = Character("Гном","7",Bow)
EsheDrugoi = Character("НеГном","1",Axe)
list = [LDFGFDGFDGD,drugoi,EsheDrugoi]
for i in list:
    i.info()