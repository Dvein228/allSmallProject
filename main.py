class Dog:
     def __init__(self,name,age,health):
          self.name= name
          self.age = age
          self.health=health
     def inroduce(self):
          print(f"Собака:{self.name},Возраст {self.age}.Собака {self.health}")



soBAKAAAAA = Dog("Бобиков","15","здорова")
soBAKAAAAA2= Dog("Крутая","13","не здорова")
soBAKAAAAA.inroduce()
soBAKAAAAA2.inroduce()