class Car:
   def __init__(self, color, millage) -> None:
      self.color = color 
      self.millage = millage

blueCar = Car("blue", 12.4)
redCar = Car("red", 15.4)

print(f"This is from {redCar.color} having millage {redCar.millage}")
print(f"This is from {blueCar.color} having millage {blueCar.millage}")

      