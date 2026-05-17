class Animal:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def voice(self,sound):
        print(f"{self.name} делает {sound}")
    def info(self):
        print(self.age,self.name)

class Cat(Animal):
    def __init__(self,wool,age,name):
        super().__init__(age, name)
        self.wool = wool
    def info(self):
        super().info()
        print(self.wool)


class Fish(Animal):
    def __init__(self,age,name,scales):
        super().__init__(age,name)
        self.scales= scales
    def info(self):
        super().info()
        print(self.scales)


carpik = Fish(1,"каРПик",True)
cotak = Cat(True,7,"Котак")
carpik.voice("Бульк")
cotak.voice("Мяу")