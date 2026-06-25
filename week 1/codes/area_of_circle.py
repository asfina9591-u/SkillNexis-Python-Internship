import math

def area_of_circle(radius):
    return math.pi * radius * radius

r = float(input("Enter radius: "))
print("Area of circle =", area_of_circle(r))
