class Enemy:
    def __init__(self, name, health):
        self.name=name
        self.health=health

    def info(self):
        print("Ім'я:", self.name)
        print("ХП:", self.health)
class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense=defense

class Weapon:
    def __init__(self, name, damage):
        self.name=name
        self.damage=damage

    def info(self):
        print("Ім'я:", self.name)
        print("Урон:", self.damage)

class Character:
    def __init__(self, name, level,weapon,Armor):
        self.name=name
        self.level=level
        self.weapon = weapon
        self.armor=Armor

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print(f"Використовує {self.weapon.name} з {self.weapon.damage} урона ")

    def attack(self, enemy):
        print(self.name, "атакує", enemy.name)
        enemy.health -= self.weapon.damage
        print(enemy.name, "отримав шкоду")
        print("HP ворога:", enemy.health)

Bow= Weapon("лук",1)
Axe= Weapon("Акс",375)

skeleton = Enemy("скелет",100)
LDFGFDGFDGD=Character("Гном-перегном",5,Bow)
drugoi = Character("Гном",7,Bow)
EsheDrugoi = Character("НеГном",1,Axe)


drugoi.attack(skeleton)