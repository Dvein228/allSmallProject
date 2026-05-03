class Dog:
     def __init__(self,name,age,health,energy):
          self.name= name
          self.age = age
          self.health=health
          self.energy = energy
     def inroduce(self):
          print(f"Собака:{self.name},Возраст {self.age}.Собака {self.health}")
     def eat(self):
          self.energy+=3
          print(f"{self.name} ест")
     def sleep(self):
          print(f"{self.name} спит")




soBAKAAAAA = Dog("Бобиков","15","здорова",0)
soBAKAAAAA2= Dog("Крутая","13","не здорова",0)

soBAKAAAAA.inroduce()
soBAKAAAAA.eat()
soBAKAAAAA.sleep()


soBAKAAAAA2.inroduce()
soBAKAAAAA2.eat()
soBAKAAAAA2.sleep()
