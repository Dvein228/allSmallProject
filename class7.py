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
    def meow(self):
        print(self.name+":мяу")
class Fish(Animal):
    def __init__(self,age,name,scales):
        super().__init__(age,name)
        self.scales= scales
    def bulk(self):
        print(self.name+":буль")


carpik = Fish(1,"каРПик",True)
cotak = Cat(True,7,"Котак")
carpik.bulk()
cotak.meow()