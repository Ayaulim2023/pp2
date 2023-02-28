import math
n =int(input("Input dedree: "))

def DegToRad(n):
    return n * math.pi/180

print("Output radian:",DegToRad(n))