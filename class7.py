class Animal:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)
    def voice(self,sound):
        print(f"{self.name} делает {sound}")

class Cat(Animal):
    def __init__(self,wool,age,name):
        super().__init__(age, name)
        self.wool = wool

class Fish(Animal):
    def __init__(self,age,name,scales):
        super().__init__(age,name)
        self.scales= scales



carpik = Fish(1,"каРПик",True)
cotak = Cat(True,7,"Котак")
carpik.voice("Бульк")
cotak.voice("Мяу")