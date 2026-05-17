class Animal:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)

class Cat(Animal):
    def __init__(self,wool,age,name):
        super().__init__(age, name)
        self.wool = wool
class Fish(Animal):
    def __init__(self,age,name,scales):
        super().__init__(age,name)
        self.scales= scales