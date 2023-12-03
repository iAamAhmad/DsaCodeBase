class Employee:
   def __init__(self, name, age) -> None:
      self.name = name
      self.age = age
   def description(self):
        return f"{self.name} is {self.age} years old"
   def speak(self, sound):
        return f"{self.name} says {sound}"
      
      
employee = Employee("Ahmad", 13)
print(employee.name)
print(employee.age)
print(employee.description())
print(employee.speak("Wohooooooooo"))


      