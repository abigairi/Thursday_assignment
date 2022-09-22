class Person:
            def __init__(self,name,age,address):
                  self.name= name
                  self.age=age
                  self.address=address
                  def __repr__(self):
                      return f"<person {self.name} {self.age} {self.address}>"
person=Person ("Abigail","15","23N street")
print(f"My name is {person.name}\n My age is {person.age}\n My address is {person.address}") 
            
print(f"{person.name} is eating")
 
print(f" {person.name} is sleeping") 
       
print(f"{person.name} is working")

