class Character:
    def __init__(self, name, level):
        self.name=name
        self.level=level

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
class Weapon:
    def __init__(self, name, damage):
        self.name=name
        self.damage=damage

    def info(self):
        print("Ім'я:", self.name)
        print("Урон:", self.damage)

LDFGFDGFDGD=Character("Гном-перегном","5")
drugoi = Character("Гном","7")
EsheDrugoi = Character("НеГном","1")
