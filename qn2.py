class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

def print_animal(self):
        print(f"{self.name} {self.color}")
        print(self.name)
        print(self.color)
                              

class Dog(Animal):
             def __init__(self, name, color,action):
                  self.action=action
                  Animal. __init__(self,name,color)

dog=Dog ("Kabaana","black","bark")
print(f"Her name is {dog.name}\n she is {dog.color}\n She does {dog.action}")
              