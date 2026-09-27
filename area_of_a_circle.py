# A programmer is developing a program that will calculate the area of a circle. Construct the code using a function or method.
# Area = pi x rˆ2
import math

def calcCircle(radius):
    area = math.pi * radius**2
    return area

r=float(input("What radius? "))
print(f"The area of the circle with radius {r} is {calcCircle(r)} units squared")