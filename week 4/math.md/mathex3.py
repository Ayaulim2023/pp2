import math
def area(a,b):
    return ((b**2)*a)/(4*math.tan(math.pi/a))

a = int(input("Input number of sides: "))
b = int(input("Input the length of a side: "))

print("The area of the polygon is:",area(a,b))